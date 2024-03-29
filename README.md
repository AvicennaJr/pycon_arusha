# Pycon Arusha

This is (some of) the source code of the tutorials presented at Pycon Arusha on 2nd March, 2024.

We built two main applications;
    - A chatbot interface
    - An AI powered text correction


## Requirements

To run any of these programs then you need the following:

- Python
- Groq API key. You can get it from: https://console.groq.com
- Ollama for the `text-correction-ollama.py` example. You can download and install ollama here: https://ollama.ai


## ChatBot Interface

There are mainly two versions, one with memory and one without. Both are presented to show the difference between the two.

The chatbot interface without memory is in the file `chatbot.py` and the one with memory is in the file `chatbot-with-memory.py`.


## AI Powered Text Correction

There are two versions of the AI powered Text correction, one uses (Groq)[https://groq.com] in the file `text-correction-groq.py` and the other uses a self hosting option with (ollama)[https://ollama.ai] in the file `text-correction-ollama.py`.


## Usage

### Install Requirements:

```bash
pip install -r requirements.txt
```

### Fill in the Groq API Key:

For the following files:
- chatbot.py
- chatbot-with-memory.py
- text-correction-groq.py

Replace `your-api-key-here` with your actual API keys, otherwise you will receive an error.

### Run the application

Choose any of the files and run it with python. For example:

```bash
python chatbot.py
```

### Notes

For the text correction example, I used the key `F9`. In `pynput` you have to specify the value of `F9` on your keyboard, which in my case is `<65478>`.

But in case that value is incorrect for you, the just open the python shell and run the following commands as shown in the screenshot below:

![Key Value](./assets/key_value.png)

Copy the value (with the brackets `<>`) and use them in the code.

> For any questions and suggestions reach out to me via telegram @JustMojo