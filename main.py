# Text-based fantasy rpg game

import os
import time
import player_character
import combat_system
import quest_manager

# Define global variables for game text
welcome_text = "Welcome to First Fantasy RPG!"

# Function for clearing the screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    return

def welcome_screen():
    clear_screen()
    print(f"{welcome_text}\n")
    print(f"\nMain Menu\n")
    print("  1. Character Menu")
    print("  2. Start Game")
    print("  3. Exit")
    choice = input("\nEnter your choice: ")
    return choice

def start_game():
    clear_screen()
    print("Starting game...")
    time.sleep(1)
    main()



def main():
    choice = welcome_screen()
    if choice == "1":
        player_character.run_menu()
        main()
    elif choice == "2":
        start_game()
    elif choice == "3":
        print("Exiting game...")
        time.sleep(1)
        clear_screen()
    else:
        print("Invalid choice. Please try again.")
        time.sleep(1)
        main()
    return




main()