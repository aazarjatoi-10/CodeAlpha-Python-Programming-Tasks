def basic_ChatBot():

    print("--- Mini ChatBot 2.0 ---\n")
    print("Bot: Hey, how can I help you?")
    
    while True:

        user_query = input("You: ").lower()

        if user_query == "who are you?":
            print("Bot: I am a rule-based chatbot.")

        elif user_query == "who created you?":
            print("Bot: I was created by Aazar as a task of CodeAlpha internship.")

        elif user_query == "what's your name?":
            print("Bot: My name is Mini ChatBot 2.0")

        elif user_query == "exit":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand that.")

basic_ChatBot()