import pyautogui as pt
from time import sleep
import pyperclip
import subprocess
import keyboard
import google.generativeai as genai
import os

# Configure Google Gemini API
genai.configure(api_key="AIzaSyDIaOBZj_WO08dmsQqHzz5057y-LYkMb_E")
model = genai.GenerativeModel('gemini-1.5-flash')
history = []
# Open WhatsApp from the Microsoft Store
subprocess.Popen(["explorer.exe", "shell:AppsFolder\\5319275A.WhatsAppDesktop_cv1g1gvanyjgm!App"])
# Give WhatsApp time to open
sleep(5)

def get_received_message():
    position = pt.locateOnScreen("smilie.png", confidence=0.7)
    if position:
        x, y = position[0], position[1]
        pt.moveTo(x + 80, y - 50, duration=0.5)  # Adjust this offset based on the position of the message
        pt.tripleClick()
        pt.hotkey('ctrl', 'c')

        pt.moveRel(10, 10)  # Adjust this to ensure you are clicking on 'Copy'
        pt.click()
        received_message = pyperclip.paste()
        print("Received Message: " + received_message)
        return received_message
    else:
        print("Smilie icon not found on the screen.")
        return ""

def send_message(message):
    position = pt.locateOnScreen("smilie.png", confidence=0.6)
    if position:
        x, y = position[0], position[1]
        pt.moveTo(x + 200, y + 20, duration=0.5)
        pt.click()
        pt.typewrite(message, interval=0.01)
        pt.typewrite("\n", interval=0.01)
        pt.press("esc") 
        pt.press("esc") # Press Escape key after sending the message
    else:
        print("Smilie icon not found on the screen.")

def generate_response(message):
    # Append user message to history
    history.append(f"User: {message}")    
    # Build the prompt with conversation history
    prompt = "Conversation History:\n"
    for entry in history:
        prompt += f"{entry}\n"
    prompt += "Prompt :You are a human bot that can reply as a human and your name is laiba and you are a girl dont give tash response give accurate according to the question like human "

    # Generate response using the model
    response = model.generate_content(prompt)
    if response:
        reply = response.text.strip()
        
        # Append generated reply to history
        history.append(f"Reply:{reply}")
        return reply
    else:
        return "Sorry, I couldn't understand that."

def check_for_unread_messages():
    while True:
        try:
            if keyboard.is_pressed('delete'):
                print("Exit script")
                break

            position = pt.locateOnScreen("unread.png", confidence=0.6)
            if position:
                pt.moveTo(position)
                pt.moveRel(-100, 0)
                pt.click()
                sleep(1)
                received_message = get_received_message()
                if received_message:
                    message_to_send = generate_response(received_message)
                    send_message(message_to_send)
                else:
                    print("No new message")
        except Exception as e:
            print("No new messages:", e)

check_for_unread_messages()