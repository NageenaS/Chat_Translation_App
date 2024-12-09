from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv
from twilio.rest import Client
import mysql.connector

# Load environment variables from .env file
load_dotenv()

# Flask app initialization
app = Flask(__name__)

# Google Translate API details
TRANSLATION_API_URL = "https://google-translator9.p.rapidapi.com/v2"
RAPIDAPI_KEY = os.getenv("RAPIDAPI_KEY")

# Fetch Twilio credentials from environment variables
account_sid = os.getenv('TWILIO_SID')
auth_token = os.getenv('TWILIO_AUTH_TOKEN')

# Create Twilio client
client = Client(account_sid, auth_token)

# Languages dictionary to pass to the template
languages = {
    "en": "English",
    "es": "Spanish",
    "fr": "French",
    "de": "German",
    "ko": "Korean",
    "ja": "Japanese",
    "hi": "Hindi",
    "gu": "Gujarati",
    "ta": "Tamil",
    "te": "Telugu",
    "kn": "Kannada",
    "bn": "Bengali",
    "ml": "Malayalam"
}

# MySQL connection setup
def get_mysql_connection():
    try:
        conn = mysql.connector.connect(
            host=os.getenv('MYSQL_HOST'),
            user=os.getenv('MYSQL_USER'),
            password=os.getenv('MYSQL_PASSWORD'),
            database=os.getenv('MYSQL_DATABASE')
        )
        return conn
    except mysql.connector.Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

# Homepage - Send Message
@app.route('/')
def index():
    return render_template("index.html", languages=languages)

# Save message to MySQL database
def save_message_to_mysql(sender, recipient, recipient_phone, message, translated_message, preferred_language):
    conn = get_mysql_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute(''' 
                INSERT INTO messages (sender, recipient, recipient_phone, message, translated_message, preferred_language)
                VALUES (%s, %s, %s, %s, %s, %s)
            ''', (sender, recipient, recipient_phone, message, translated_message, preferred_language))
            conn.commit()
            cursor.close()
        except mysql.connector.Error as e:
            print(f"Error saving message to database: {e}")
        finally:
            conn.close()

# Send Message API
@app.route('/send-message', methods=['POST'])
def send_message():
    data = request.form
    sender = data['sender']
    recipient = data['recipient']
    recipient_phone = data['number']
    message = data['message']
    preferred_language = data['preferred_language']

    # Fetch recipient's settings
    translated_message = translate_message(message, preferred_language)

    # Save the message to the database
    save_message_to_mysql(sender, recipient, recipient_phone, message, translated_message, preferred_language)

    # Send the message to recipient's WhatsApp
    send_whatsapp_message(recipient_phone, translated_message)

    return render_template("index.html", sender=sender, 
                           recipient=recipient, phone_number=recipient_phone,
                           original_message=message, translated_message=translated_message,
                           languages=languages)

# Function to Translate Message
def translate_message(message, target_language):
    headers = {
        "x-rapidapi-key": RAPIDAPI_KEY,
        "x-rapidapi-host": "google-translator9.p.rapidapi.com",
        "Content-Type": "application/json",
    }
    payload = {
        "q": message,
        "source": "en",
        "target": target_language,
        "format": "text"
    }

    # Call Google Translate API
    response = requests.post(TRANSLATION_API_URL, json=payload, headers=headers)

    if response.status_code != 200:
        return f"Error: Unable to translate message ({response.text})"

    translated_message = response.json().get("data", {}).get("translations", [{}])[0].get("translatedText", message)
    return translated_message

# Function to Send WhatsApp Message via Twilio
def send_whatsapp_message(phone_number, message):
    client.messages.create(
        to=f"whatsapp:{phone_number}",
        from_="whatsapp:+14155238886",  # Twilio sandbox WhatsApp number
        body=message
    )

# View Messages API
@app.route('/view-messages')
def view_messages():
    conn = get_mysql_connection()
    if conn:
        try:
            cursor = conn.cursor()
            cursor.execute('SELECT sender, recipient, message, translated_message, preferred_language, timestamp FROM messages')
            messages = cursor.fetchall()
            cursor.close()
        except mysql.connector.Error as e:
            print(f"Error retrieving messages: {e}")
            messages = []
        finally:
            conn.close()

        # Pass 'languages' dictionary to the template along with messages
        return render_template("view_messages.html", messages=messages, languages=languages)
    else:
        return "Error connecting to the database", 500


if __name__ == "__main__":
    app.run(debug=True)
