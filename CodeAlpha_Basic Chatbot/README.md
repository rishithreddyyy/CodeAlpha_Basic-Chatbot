# Basic Rule-Based Chatbot

A simple, interactive rule-based chatbot built in Python for the **CodeAlpha** internship task.

---

## 📌 Project Overview
The goal of this project is to create a simple chatbot that matches user input against predefined rules and responds accordingly.

### Scope & Predefined Replies
- **User input:** `"hello"`, `"hi"`, `"how are you"`, `"what is your name"`, `"bye"`, etc.
- **Predefined replies:**
  - Greetings: `"Hi! How can I help you today?"`
  - Well-being: `"I'm fine, thanks! How about you?"`
  - Identity: `"I am a simple rule-based chatbot built with Python."`
  - Farewell: `"Goodbye! Have a wonderful day!"`
  - Fallback: `"I'm sorry, I don't understand that. Type 'help' to see what you can ask me."`

---

## 🔑 Key Concepts Used

| Concept | Implementation in Code |
| :--- | :--- |
| **Functions** | `get_response(user_input)` handles NLP rule matching; `run_chatbot()` controls the execution flow. |
| **Conditional Statements (`if-elif-else`)** | Evaluates normalized user input against defined keywords and conditions. |
| **Loops (`while`)** | Keeps the interactive conversation active until an exit command (`bye`, `quit`, `exit`) is entered. |
| **Input / Output (`input()`, `print()`)** | Prompts user for input and displays styled responses in the terminal. |

---

## 🚀 How to Run

### Prerequisites
- Python 3.x installed on your machine.

### 1. Run the Chatbot
Open your terminal in this directory and run:
```bash
python chatbot.py
```

### 2. Run the Unit Tests
To verify all rule sets and boundary conditions:
```bash
python -m unittest test_chatbot.py
```

---

## 💬 Example Interaction

```text
==================================================
        WELCOME TO BASIC RULE-BASED CHATBOT       
==================================================
Type 'help' for options, or type 'bye' to exit.

You: hello
Bot: Hi! How can I help you today?

You: how are you
Bot: I'm fine, thanks! How about you?

You: what is your name
Bot: I am a simple rule-based chatbot built with Python.

You: help
Bot: You can talk to me with simple phrases like:
  - 'hello' or 'hi'
  - 'how are you'
  - 'what is your name'
  - 'thanks'
  - 'bye' to exit the chat

You: bye
Bot: Goodbye! Have a wonderful day!

[Chat session ended. Thank you for chatting!]
```

