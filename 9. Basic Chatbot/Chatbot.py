import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime

# Basic chatbot logic
def respond_to_user(input_text):
    input_text = input_text.lower()

    if "hello" in input_text or "hi" in input_text:
        return "Hello! How can I help you today?"
    elif "how are you" in input_text:
        return "I'm just a bunch of code, but I'm doing great! 😄"
    elif "your name" in input_text:
        return "I'm ChatBot, your virtual assistant."
    elif "help" in input_text:
        return "Sure! You can ask me about the weather, time, or just chat."
    elif "weather" in input_text:
        return "I can't access live data yet, but it's always sunny in Python land! 🌞"
    elif "time" in input_text:
        return f"The current time is {datetime.now().strftime('%I:%M %p')}."
    elif "bye" in input_text:
        return "Goodbye! Have a great day! 👋"
    else:
        return "I'm not sure how to respond to that."

# Handle send button click
def send_message():
    user_message = entry_box.get()
    if user_message.strip() == "":
        return

    chat_box.config(state=tk.NORMAL)
    chat_box.insert(tk.END, "You: " + user_message + "\n")
    entry_box.delete(0, tk.END)

    bot_response = respond_to_user(user_message)
    chat_box.insert(tk.END, "Bot: " + bot_response + "\n\n")
    chat_box.config(state=tk.DISABLED)
    chat_box.yview(tk.END)  # Scroll to bottom

# GUI setup
window = tk.Tk()
window.title("Python ChatBot")
window.geometry("500x600")

# Chat history
chat_box = scrolledtext.ScrolledText(window, state=tk.DISABLED, wrap=tk.WORD, font=("Arial", 12))
chat_box.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

# Entry and send button
frame = tk.Frame(window)
entry_box = tk.Entry(frame, font=("Arial", 14))
entry_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
send_button = tk.Button(frame, text="Send", font=("Arial", 14), command=send_message)
send_button.pack(side=tk.RIGHT)
frame.pack(padx=10, pady=10, fill=tk.X)

# Optional: Pressing Enter triggers send
window.bind('<Return>', lambda event: send_message())

window.mainloop()
