def basic_chatbot():
    print("Chatbot: Hello! I am your chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input in ["hello", "hi", "hey"]:
            print("Chatbot: Hi! Nice to meet you.")

        elif user_input in ["how are you", "how r you"]:
            print("Chatbot: I'm fine, thanks for asking!")

        elif user_input == "what is your name":
            print("Chatbot: My name is chatbot.")

        elif user_input == "what can you do":
            print("Chatbot: I can answer simple questions and chat with you.")

        elif user_input in ["help", "support"]:
            print("Chatbot: You can say hello, ask how I am, or say bye.")

        elif user_input == "time":
            print("Chatbot: I cannot tell time yet, but I'm learning!")

        elif user_input in ["thank you", "thanks"]:
            print("Chatbot: You're welcome!")

        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day 😊")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")
basic_chatbot()