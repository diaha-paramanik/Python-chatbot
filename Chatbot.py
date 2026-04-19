import datetime

def chatbot():
    print("🤖 Chatbot: Hello! I am your Python Chatbot. Type 'bye' to exit.")

    while True:
        user = input("You: ").lower()

        if user in ["hello", "hi", "hey"]:
            print("🤖 Chatbot: Hello! How can I help you?")

        elif "name" in user:
            print("🤖 Chatbot: I am a simple Python chatbot created by Disha.")

        elif "time" in user:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"🤖 Chatbot: Current time is {current_time}")

        elif "date" in user:
            current_date = datetime.datetime.now().strftime("%d-%m-%Y")
            print(f"🤖 Chatbot: Today's date is {current_date}")

        elif "how are you" in user:
            print("🤖 Chatbot: I am just a bot, but I'm doing great!")

        elif "help" in user:
            print("🤖 Chatbot: You can ask me about time, date, or just say hello!")

        elif user == "bye":
            print("🤖 Chatbot: Goodbye! Have a nice day 😊")
            break

        else:
            print("🤖 Chatbot: Sorry, I don't understand that.")


chatbot()
 
