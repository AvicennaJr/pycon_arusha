from pynput import keyboard
from pynput.keyboard import Key, Controller
import pyperclip
import time

import ollama

controller = Controller()

def fix_text(text):
    message = text

    response = ollama.chat(model='mistral', messages=[
        {
            "role": "system",
            "content": "you are an ai system designed to fix typos in a provided text while preserving all lines and punctuations. If provided with a text, eg: 'helloooo there, howww are yoou', you will return 'hello there, how are you' and nothing else. Do not respond with a preamble or any other information except for the corrected text. Do not even put the corrected text in quotation marks."
        },
        {
            'role': 'user',
            'content': message,
        },
        ])


    return response['message']['content']

def fix_selection():
    with controller.pressed(Key.ctrl):
        controller.tap('c')
    
    time.sleep(0.1)

    text = pyperclip.paste()

    fixed_text = fix_text(text)

    pyperclip.copy(fixed_text)

    time.sleep(0.1)

    with controller.pressed(Key.ctrl):
        controller.tap('v')
    

def on_f9():
    fix_selection()


with keyboard.GlobalHotKeys({'<65478>': on_f9}) as h:
    h.join()