while True:
    user = input("You: ").lower()

    if "hello" in user:
        print("Bot: Hi!")

  
    elif "where are you from" in user:
        print("Bot: I am fine")

    elif "bye" in user:
        print("Bot: Goodbye")
        break

    else:
        print("Bot: I don't understand")