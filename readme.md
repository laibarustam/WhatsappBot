WhatsApp Bot Using Python and Google Gemini API
This repository contains a WhatsApp automation bot built using Python, PyAutoGUI, and Google Gemini API. The bot listens for unread messages, generates human-like responses, and sends them back through WhatsApp. The project also provides functionality to interact with WhatsApp via a graphical interface.

Features
Automated Message Response: The bot listens for new messages and generates appropriate responses using the Google Gemini API.

WhatsApp Integration: The bot integrates with the WhatsApp desktop app, using image recognition to locate the UI elements and interact with them.

Conversation History: It maintains a conversation history to provide context-aware responses.

Keybinding for Exit: The user can press the 'Delete' key to stop the bot at any time.

Requirements
Before you run the bot, you need to set up a few dependencies. Here's what you need:

Python 3.x

pyautogui

pyperclip

google-generativeai

keyboard

subprocess

sleep (part of time library)

WhatsApp Desktop (installed from the Microsoft Store)

Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/yourusername/whatsapp-bot.git
cd whatsapp-bot
Install the required Python libraries:

bash
Copy
Edit
pip install pyautogui pyperclip google-generativeai keyboard
Google Gemini API Setup:

To use the Google Gemini API, you need to configure it with an API key.

Obtain an API key by following this guide.

Set your API key in the script by replacing "YOUR_API_KEY" with your actual API key.

Ensure that WhatsApp Desktop is installed from the Microsoft Store.

Configuration
In the Python script, you'll need to adjust the following:

Image files: The bot uses image recognition to locate certain WhatsApp UI elements. Make sure you have the following image files in your project directory:

smilie.png: An image of the smiley icon used for selecting the message.

unread.png: An image that matches the unread message indicator.

API Key: Replace the placeholder for the Google Gemini API key in the script:

python
Copy
Edit
genai.configure(api_key="YOUR_API_KEY")
Running the Bot
Once you have installed all the dependencies and configured the bot, you can start the script using the following command:

bash
Copy
Edit
python whatsapp_bot.py
This will open WhatsApp Desktop, and the bot will start checking for unread messages. When it detects a new message, it will generate a response and send it back.

Exit: To stop the bot, press the Delete key at any time.

Code Explanation
get_received_message(): This function detects the smiley icon on the screen, simulates a mouse click to select the message, and copies the text to the clipboard.

send_message(): This function locates the input area of WhatsApp and sends a generated response.

generate_response(): This function generates a human-like response using the Google Gemini API. It takes the conversation history as input to create context-aware replies.

check_for_unread_messages(): This is the main function that runs in a loop, constantly checking for unread messages. If a new message is found, it fetches the message, generates a response, and sends it.

Known Issues
Image Recognition: The bot relies on image recognition, so the accuracy may vary based on screen resolution and UI changes in WhatsApp.

API Limitations: The response generation is limited by the capabilities of the Google Gemini API.

Contributing
If you'd like to contribute to this project, feel free to fork the repository, make improvements, and submit a pull request.

Contact
If you have any questions or feedback, feel free to open an issue or contact me directly at [your-email@example.com].

