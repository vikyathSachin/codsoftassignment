import tkinter as tk
import random

# Predefined responses
responses = {
    "hello": ["Hi there! How can I assist you?", "Hello! How's your day going?", "Hey! What can I do for you?"],
    "bye": ["Goodbye! Have a great day!", "See you later! Take care!", "Bye! Don't forget to come back soon!"],
    "how are you": ["I'm just a bot, but I'm doing great! How about you?", "I'm functioning perfectly, thank you!"],
    "what's your name": ["I'm your friendly chatbot!", "You can call me ChatBot 101."],
    "who created you": ["I was created by Sachin!", "A brilliant person named Sachin made me!"],
    "what is artificial intelligence": [
        "Artificial Intelligence is the simulation of human intelligence in machines.",
        "AI stands for Artificial Intelligence, enabling machines to think and act like humans."
    ],
    "tell me a joke": [
        "Why don't scientists trust atoms? Because they make up everything!",
        "Why was the math book sad? It had too many problems.",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ],
    "what is your purpose": [
        "My purpose is to assist you and make your day better!",
        "I'm here to chat and provide any help you need."
    ]
}

# Function to handle user input
def chatbot_response(user_input):
    user_input = user_input.lower()
    # Check for keyword matches
    for key in responses:
        if key in user_input:
            return random.choice(responses[key])
    # Default fallback response
    return "I'm sorry, I don't understand that. Can you rephrase?"

# Send message function
def send_message():
    user_message = user_input.get()
    if user_message.lower() == "bye":
        chat_log.insert(tk.END, "You: " + user_message + "\n")
        chat_log.insert(tk.END, "Chatbot: Goodbye! Have a great day!\n")
        root.destroy()
    else:
        bot_response = chatbot_response(user_message)
        chat_log.insert(tk.END, "You: " + user_message + "\n")
        chat_log.insert(tk.END, "Chatbot: " + bot_response + "\n")
    user_input.delete(0, tk.END)

# Create the GUI
root = tk.Tk()
root.title("Chatbot")

# Chat log
chat_log = tk.Text(root, bg="white", fg="black", width=50, height=20)
chat_log.grid(row=0, column=0, columnspan=2)

# User input field
user_input = tk.Entry(root, bg="white", fg="black", width=40)
user_input.grid(row=1, column=0)

# Send button
send_button = tk.Button(root, text="Send", command=send_message)
send_button.grid(row=1, column=1)

# Run the GUI
root.mainloop()
