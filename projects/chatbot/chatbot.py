# Simple AI Chatbot Demo

print("AI Chatbot 🤖")
print("Type 'exit' to stop.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Bot: Goodbye!")
        break

    if "hello" in user_input.lower():
        print("Bot: Hello! Nice to meet you.")

    elif "name" in user_input.lower():
        print("Bot: I am a simple AI chatbot.")

    elif "how are you" in user_input.lower():
        print("Bot: I am working well!")

    else:
        print("Bot: I am still learning.")
