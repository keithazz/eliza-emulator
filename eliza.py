#!/usr/bin/env python3

import os
from colorama import init, Fore, Back, Style

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

def main():
    # Set up terminal
    clear_screen()
    print(Back.BLACK + Fore.WHITE + Style.BRIGHT, end="")
    print_header()
    
    # Initial conversation
    print(f"{Fore.WHITE}ELIZA: Is something troubling you ?")
    
    while True:
        try:
            # Get user input for Jamie's response
            print(f"{Fore.WHITE}YOU  :", end=" ")
            jamie_input = input()
            
            # Get user input for ELIZA's response
            print(f"{Fore.WHITE}ELIZA:", end=" ")
            eliza_input = input()
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    try:
        main()
    finally:
        # Reset terminal colors on exit
        print(Style.RESET_ALL) 