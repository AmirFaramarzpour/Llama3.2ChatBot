import os
import customtkinter as ctk
from gtts import gTTS
import pygame
from PIL import Image
import tkinter as tk

def generate_response(prompt):
    response = os.popen(f"ollama run llama3.2 '{prompt}'").read()
    return response.strip()

def text_to_speech(text, lang='en', tld='co.uk'):
    if text:
        tts = gTTS(text, lang=lang, slow=False, tld=tld)
        tts.save("response.mp3")
        pygame.mixer.init()
        pygame.mixer.music.load("response.mp3")
        pygame.mixer.music.play()
    else:
        print("No text to speak.")

def on_submit():
    prompt = prompt_entry.get("1.0", 'end-1c')
    response = generate_response(prompt)
    chat_history.configure(state=ctk.NORMAL)
    chat_history.insert(ctk.END, "You:	" + prompt + "\n")
    chat_history.insert(ctk.END, "Llama3.2:	" + response + "\n\n")
    chat_history.configure(state=ctk.DISABLED)
    chat_history.yview(ctk.END)
    prompt_entry.delete("1.0", ctk.END)
    # Store the latest response globally
    global latest_response
    latest_response = response

def on_vocal():
    try:
        text_to_speech(latest_response)
    except NameError:
        print("No response to vocalize")

if __name__ == "__main__":
    ctk.set_appearance_mode("dark")  # Modes: "dark", "light"
    ctk.set_default_color_theme("blue")  # Themes: "blue", "green", "dark-blue"

    app = ctk.CTk()
    app.title("Ollama Llama 3.2 Chat")
    app.geometry("400x400")
    app.resizable(False,False)

    # Labels
    chat_history_label = ctk.CTkLabel(app, text="Chat History")
    chat_history_label.pack(pady=(10, 0))

    # Set up the chat history area
    chat_history = ctk.CTkTextbox(app, wrap=ctk.WORD, width=380, height=150)
    chat_history.pack(padx=10, pady=10)
    chat_history.configure(state=ctk.DISABLED)

    # Prompt box label
    prompt_entry_label = ctk.CTkLabel(app, text="Prompt Box")
    prompt_entry_label.pack(pady=(10, 0))

    # Set up the prompt entry area
    prompt_entry = ctk.CTkTextbox(app, wrap=ctk.WORD, width=380, height=50)
    prompt_entry.pack(padx=10, pady=10)

    # Set up the submit button
    submit_button = ctk.CTkButton(app, text="Submit", command=on_submit)
    submit_button.pack(pady=5)

    # Use a Unicode speaker symbol for the vocal button
    vocal_button = ctk.CTkButton(app, text="Listen 🔊", command=on_vocal)
    vocal_button.pack(pady=5)

    app.mainloop()
