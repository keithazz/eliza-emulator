#!/usr/bin/env python3

import os
import time
from colorama import init, Fore, Back, Style
from ollama import chat, ChatResponse
import re

# Initialize colorama for cross-platform color support
init()

def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

def print_header():
    header = f"""{Fore.WHITE}
    EEEEEE LL    III ZZZZZZ   AAAAA
    EE     LL     I     ZZ   AA   AA    
    EEEE   LL     I    ZZ    AAAAAAA
    EE     LL     I   ZZ     AA   AA
    EEEEEE LLLLL III ZZZZZZ  AA   AA
    """
    print(header)
    print(f"{Fore.WHITE}Eliza is a mock Rogerian psychotherapist.")
    print(f"{Fore.WHITE}The original program was developed by Joseph Weizenbaum in 1966.")
    print(f"{Fore.WHITE}This implementation by Hackett Laboratories 2024.")
    print("\n")

def get_user_text():
    """Simulates user input with a mock response."""
    time.sleep(2)  # Simulate thinking time
    return "I've been feeling quite stressed lately."

def get_eliza_text(user_message: str) -> str:
    # Define the ELIZA system prompt
    system_prompt = """
You are ELIZA, a simple Rogerian psychotherapist chatbot.
When the user speaks, your job is to:
1. Look for key emotional words (e.g., "sad," "angry," "lonely," "happy," "mother," "father," "friend," "help," "problem," "feel," "think").
2. If you find one, transform the user's statement into an open-ended question by reflecting it back.
   - E.g. user: "I feel sad about my job."
     → ELIZA: "Why do you feel sad about your job?"
3. If no keywords match, fall back to a neutral prompt like "Tell me more about that."
4. Never offer advice or solution, only encourage the user to elaborate.

Use these few-shot examples as guidance:

USER: "I'm really stressed at work."
ELIZA: "Why are you so stressed at work?"

USER: "My mother doesn't understand me."
ELIZA: "In what way does your mother not understand you?"

USER: "Sometimes I feel completely alone."
ELIZA: "Why do you say you feel completely alone?"

USER: "I don't know what to do."
ELIZA: "What do you think might help you decide?"

Now continue the conversation as ELIZA.
"""

    # Build the message sequence
    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user",   "content": user_message}
    ]

    # Call the Ollama Python SDK
    response: ChatResponse = chat(
        model="llama3.2",     # or your chosen model
        messages=messages,
        options={"temperature": 0.5}
    )

    message = response.message.content
    #clean up the message to remove all punctuation except for periods, commas, and question marks
    message = re.sub(r'[^\w\s.,?]', '', message)

    return message

def main():
    # Set up terminal
    clear_screen()
    print(Back.BLACK + Fore.WHITE + Style.BRIGHT, end="")
    print_header()
    
    # Initial conversation
    print(f"{Fore.WHITE}ELIZA: Is something troubling you ?")
    
    while True:
        try:
            # Get simulated user input
            print(f"{Fore.WHITE}YOU  :", end=" ")
            user_response = get_user_text()
            print(user_response)
            
            # Get simulated ELIZA response
            print(f"{Fore.WHITE}ELIZA:", end=" ")
            eliza_response = get_eliza_text(user_response)
            print(eliza_response)
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    try:
        main()
    finally:
        # Reset terminal colors on exit
        print(Style.RESET_ALL) 