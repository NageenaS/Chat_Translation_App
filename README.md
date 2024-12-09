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
3. **Deploy with Docker**:
You can quickly deploy the application using Docker. Follow these steps:
Pull the pre-built image:
```
docker pull nageenashaik/chat_translation_app
```
- Start the container:
```
docker run -d --name chat-translationa-app nageenashaik/chat_translation_app
```
- If you're running it in a Docker container:
```
docker exec -it chat-translationa-app 
```

4. **Set Up Environment Variables**:
   
Create a .env file in the root directory

5. **Database Schema**:

To save messages, set up the database schema using your mysql credentials

# Run the App
After setting up the dependencies and database, run the application using:

```bash
python app.py
```
The application will be accessible at:
```bash
http://localhost:5000/
```

## Usage

After launching the application, you can:

- Send WhatsApp messages via Twilio with optional translation to the recipient's preferred language.
- View the sent message history and status through the "View Messages" section.
  ![Screenshot 2024-11-18 170853](https://github.com/user-attachments/assets/9ec42476-08cf-4437-a6bf-0b71f604bd09)
  ![Screenshot 2024-11-19 124458](https://github.com/user-attachments/assets/f29de288-eac8-41c7-a89f-a052e03027a1)

## Docker Hub
Docker Hub is a cloud-based repository that allows users to store, share, and manage Docker images. The StockApp is also available on Docker Hub. 
You can find the image [here](https://hub.docker.com/r/nageenashaik/chat_translation_app) (replace with your actual Docker Hub link). This allows you to easily deploy the application without building the image locally.



