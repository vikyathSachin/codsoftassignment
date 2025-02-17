import re

def chatbot():
    print("Hello! I am a rule-based chatbot. How can I assist you today?")

    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["exit", "quit", "bye"]:
            print("Chatbot: Goodbye! Have a great day!")
            break

        # Rule-based responses
        elif "hello" in user_input or "hi" in user_input:
            print("Chatbot: Hello! How can I help you today?")

        elif "how are you" in user_input:
            print("Chatbot: I'm just a program, but I'm functioning as expected! How about you?")

        elif "your name" in user_input:
            print("Chatbot: I am a simple rule-based chatbot.")

        elif re.search(r"what\s+is\s+your\s+purpose", user_input):
            print("Chatbot: My purpose is to assist you with your queries based on predefined rules.")

        elif re.search(r"time|date", user_input):
            from datetime import datetime
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            print(f"Chatbot: The current date and time is {current_time}.")

        elif "help" in user_input:
            print("Chatbot: Sure! I can respond to greetings, tell you the current date and time, and more. Just ask!")

        else:
            print("Chatbot: I'm sorry, I didn't understand that. Can you try rephrasing your question?")

if __name__ == "__main__":
    chatbot()
