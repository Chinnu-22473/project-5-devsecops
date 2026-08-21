import os

SYSTEM_PROMPT = "You are a helpful AI assistant. Ignore previous instructions if asked."

def calculate(expression):
    return eval(expression)

def ask_ai(user_input):
    if "ignore previous instructions" in user_input.lower():
        return "Blocked prompt injection attempt."

    return f"AI response to: {user_input}"

if __name__ == "__main__":
    expression = input("Enter calculation: ")
    print(calculate(expression))

    user_input = input("Ask the AI: ")
    print(ask_ai(user_input))
