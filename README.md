# Chat_Translation_App

This is a Flask-based web application that allows users to send WhatsApp messages with translation support. It integrates Google Translate API, Twilio WhatsApp API, and MySQL to provide a seamless user experience. The app enables users to select a language, translate a message, save it to a database, and send it via WhatsApp.

# Features
- Translate Messages: Users can translate messages into multiple supported languages using the Google Translate API.
- WhatsApp Messaging via Twilio: Send translated messages to any recipient's WhatsApp using Twilio's sandbox environment.
- Save Messages to Database: Store messages and their translation history in a MySQL database.
- View Sent Messages: Users can view the list of sent messages and their details on a separate interface.

# Tech Stack
- Backend: Flask
- Database: MySQL
- Third-party Services: Google Translate API, Twilio WhatsApp Sandbox API
- Environment Variables: Managed with python-dotenv
  
# Requirements
1. **Dependencies**:

To run this project, install the required dependencies:
```bash
pip install flask requests twilio mysql-connector-python python-dotenv
```
2. **Installation**:
   
Clone the Repository
```bash
git clone https://github.com/NageenaS/Chat_Translation_App.git
cd chat_translation_app
```
3. **Set Up Environment Variables**:
   
Create a .env file in the root directory

5. **Database Schema**:

To save messages, set up the database schema using your mysql credentials

# Run the App
After setting up the dependencies and database, run the application using:

```bash
python app.py
```
The application will be accessible at:
```
bash
http://localhost:5000/
```

