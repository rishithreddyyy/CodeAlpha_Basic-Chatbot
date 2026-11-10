"""
Basic Rule-Based Chatbot
Task: CodeAlpha - Basic Chatbot
Key Concepts Used:
    - Functions (def)
    - Conditional statements (if-elif-else)
    - Loops (while)
    - Input/Output (input(), print())
"""

def get_response(user_input: str) -> str:
    """
    Takes user input, processes it, and returns a predefined response
    using rule-based if-elif-else logic.
    """
    # Normalize input: convert to lowercase and remove leading/trailing whitespace
    cleaned_input = user_input.strip().lower()

    # Rule 1: Greeting
    if cleaned_input in ["hello", "hi", "hey", "hello there", "greetings"]:
        return "Hi! How can I help you today?"

    # Rule 2: Inquiry about well-being
    elif cleaned_input in ["how are you", "how are you doing", "how's it going", "how are you?"]:
        return "I'm fine, thanks! How about you?"

    # Rule 3: Chatbot identity
    elif cleaned_input in ["what is your name", "what's your name", "who are you", "who are you?"]:
        return "I am a simple rule-based chatbot built with Python."

    # Rule 4: Small talk / courtesy
    elif cleaned_input in ["i am fine", "i'm good", "doing well", "good"]:
        return "Glad to hear that! How can I assist you further?"

    # Rule 5: Gratitude
    elif cleaned_input in ["thank you", "thanks", "thanks a lot"]:
        return "You're welcome! Let me know if you need anything else."

    # Rule 6: Help command
    elif cleaned_input in ["help", "what can you do", "commands"]:
        return (
            "You can talk to me with simple phrases like:\n"
            "  - 'hello' or 'hi'\n"
            "  - 'how are you'\n"
            "  - 'what is your name'\n"
            "  - 'thanks'\n"
            "  - 'bye' to exit the chat"
        )

    # Rule 7: Farewell
    elif cleaned_input in ["bye", "goodbye", "see you", "exit", "quit"]:
        return "Goodbye! Have a wonderful day!"

    # Fallback response when no rule matches
    else:
        return "I'm sorry, I don't understand that. Type 'help' to see what you can ask me."


def run_chatbot():
    """
    Main function that runs the chatbot loop and handles user input/output.
    """
    print("=" * 50)
    print("        WELCOME TO BASIC RULE-BASED CHATBOT       ")
    print("=" * 50)
    print("Type 'help' for options, or type 'bye' to exit.\n")

    # Main conversation loop
    while True:
        try:
            # Taking user input
            user_input = input("You: ")
        except (KeyboardInterrupt, EOFError):
            print("\nBot: Goodbye! Have a wonderful day!")
            break

        # Check if the user entered empty input
        if not user_input.strip():
            print("Bot: Please say something! Type 'help' if you're not sure what to ask.")
            continue

        # Get response using rule-based function
        response = get_response(user_input)

        # Output bot response
        print(f"Bot: {response}")

        # Check if user wants to exit
        if user_input.strip().lower() in ["bye", "goodbye", "exit", "quit"]:
            break

    print("\n[Chat session ended. Thank you for chatting!]")


if __name__ == "__main__":
    run_chatbot()

