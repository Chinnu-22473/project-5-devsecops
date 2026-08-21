import os
import ast

SYSTEM_INSTRUCTIONS = os.getenv(
    "AI_SYSTEM_INSTRUCTIONS",
    "You are a helpful AI assistant."
)

def calculate(expression):
    try:
        return ast.literal_eval(expression)
    except (ValueError, SyntaxError):
        return "Invalid expression"

def ask_ai(user_input):
    return f"AI response to: {user_input}"

if __name__ == "__main__":
    expression = input("Enter calculation: ")
    print(calculate(expression))

    user_input = input("Ask the AI: ")
    print(ask_ai(user_input))
