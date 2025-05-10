

---

# WhatsApp Bot Using Python and Google Gemini API

A WhatsApp automation bot built using Python, PyAutoGUI, and Google Gemini API. The bot listens for unread messages, generates human-like responses, and sends them back through WhatsApp. The bot integrates with the WhatsApp Desktop app, automating interactions based on messages received.

## Table of Contents

* [Features](#features)
* [Requirements](#requirements)
* [Installation](#installation)

  * [Clone the Repository](#clone-the-repository)
  * [Install Dependencies](#install-dependencies)
  * [Configure Google Gemini API](#configure-google-gemini-api)
* [How to Run the Bot](#how-to-run-the-bot)
* [Code Explanation](#code-explanation)
* [Known Issues](#known-issues)
* [Contributing](#contributing)
* [Contact](#contact)

## Features

* **Automated Message Response**: The bot listens for incoming messages and generates appropriate responses using the Google Gemini API.
* **WhatsApp Desktop Integration**: The bot interacts with the WhatsApp Desktop application via image recognition to locate UI elements.
* **Context-Aware Conversations**: Maintains conversation history for more natural, context-aware replies.
* **Keybinding for Exiting**: Press the **Delete** key to stop the bot at any time.

## Requirements

Before you run the bot, you will need the following:

* **Python 3.x**: Ensure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).
* **Libraries**:

  * `pyautogui` for automating GUI interactions.
  * `pyperclip` for clipboard management.
  * `google-generativeai` for interfacing with the Google Gemini API.
  * `keyboard` for detecting key presses.
* **WhatsApp Desktop**: Installed via the Microsoft Store.

### Install the Required Libraries

```bash
pip install pyautogui pyperclip google-generativeai keyboard
```

## Installation

### Clone the Repository

1. First, clone the repository to your local machine:

```bash
git clone https://github.com/yourusername/whatsapp-bot.git
cd whatsapp-bot
```

### Install Dependencies

2. Install the required dependencies by running the following command:

```bash
pip install -r requirements.txt
```

*Note: Create a `requirements.txt` file with the following contents for convenience:*

```
pyautogui
pyperclip
google-generativeai
keyboard
```

### Configure Google Gemini API

1. **Obtain an API Key**:

   * To use the Google Gemini API, you need an API key. Follow [this guide](https://cloud.google.com/docs/authentication/getting-started) to obtain an API key.
   * Add your API key to the script by replacing the placeholder `"YOUR_API_KEY"`:

```python
genai.configure(api_key="YOUR_API_KEY")
```

2. **Image Files**: The bot uses image recognition to detect UI elements within WhatsApp. Make sure to have the following images in your project directory:

   * `smilie.png`: The smiley icon image for detecting the message area.
   * `unread.png`: The image used to detect unread messages.

## How to Run the Bot

Once you have installed the dependencies and configured the bot, you can run the bot using the following command:

```bash
python whatsapp_bot.py
```

This will open WhatsApp Desktop, and the bot will start checking for unread messages. When a new message is received, it will generate a response and send it back.

* **Exit**: Press the **Delete** key to stop the bot.

## Code Explanation

### `get_received_message()`

* This function searches for the smiley icon (`smilie.png`) on the screen.
* Once found, it simulates a mouse click to select the message, then copies it to the clipboard using `pyperclip`.

### `send_message()`

* Finds the input area of WhatsApp based on the smiley icon (`smilie.png`) location.
* Types out and sends the generated message to the chat window.

### `generate_response()`

* Takes the conversation history as input and generates a human-like response using the Google Gemini API.
* The response is added to the conversation history for context in future messages.

### `check_for_unread_messages()`

* Continuously checks for unread messages in WhatsApp.
* When a new message is detected, it fetches the message, generates a response, and sends it back.
* The bot runs in an infinite loop and can be exited by pressing the **Delete** key.

## Known Issues

* **Image Recognition**: The bot uses image recognition, which may not be accurate if your screen resolution or the WhatsApp UI changes.
* **API Limitations**: The Google Gemini API has limitations on the number of requests and may not always generate accurate responses depending on the input.

## Contributing

Contributions are welcome! If you'd like to improve the bot or add new features, feel free to fork the repository, make changes, and submit a pull request.

### How to Contribute

1. Fork the repository.
2. Clone your forked repository:

```bash
git clone https://github.com/yourusername/whatsapp-bot.git
```

3. Create a new branch:

```bash
git checkout -b new-feature
```

4. Make your changes and commit them:

```bash
git commit -m "Add new feature"
```

5. Push your changes:

```bash
git push origin new-feature
```

6. Submit a pull request from your fork to the main repository.

## Contact

If you have any questions or feedback, feel free to open an issue or contact me directly at \[[(laibarustam858@gmail.com)].


