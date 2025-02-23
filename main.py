# Text-based fantasy rpg game

import os
import sys
import time
import player_character
import combat_system
import quest_manager

# Define global variables
current_character = player_character.current_character

# Function for clearing the screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    return

def welcome_screen():
    clear_screen()
    print("          _______  _        _______  _______  _______  _______   _________ _______                                                            ")
    print("|\     /|(  ____ \( \      (  ____ \(  ___  )(       )(  ____ \  \__   __/(  ___  )                                                           ")
    print("| )   ( || (    \/| (      | (    \/| (   ) || () () || (    \/     ) (   | (   ) |                                                           ")
    print("| | _ | || (__    | |      | |      | |   | || || || || (__         | |   | |   | |                                                           ")
    print("| |( )| ||  __)   | |      | |      | |   | || |(_)| ||  __)        | |   | |   | |                                                           ")
    print("| || || || (      | |      | |      | |   | || |   | || (           | |   | |   | |                                                           ")
    print("| () () || (____/\| (____/\| (____/\| (___) || )   ( || (____/\     | |   | (___) |                                                           ")
    print("(_______)(_______/(_______/(_______/(_______)|/     \|(_______/     )_(   (_______)                                                           ")
    print("                                                                                                                                            ")
    print(" _______ _________ _______  _______ _________   _______  _______  _       _________ _______  _______             _______  _______  _______  _ ")
    print("(  ____ \\\__   __/(  ____ )(  ____ \\\__   __/  (  ____ \(  ___  )( (    /|\__   __/(  ___  )(  ____ \|\     /|  (  ____ )(  ____ )(  ____ \( )")
    print("| (    \/   ) (   | (    )|| (    \/   ) (     | (    \/| (   ) ||  \  ( |   ) (   | (   ) || (    \/( \   / )  | (    )|| (    )|| (    \/| |")
    print("| (__       | |   | (____)|| (_____    | |     | (__    | (___) ||   \ | |   | |   | (___) || (_____  \ (_) /   | (____)|| (____)|| |      | |")
    print("|  __)      | |   |     __)(_____  )   | |     |  __)   |  ___  || (\ \) |   | |   |  ___  |(_____  )  \   /    |     __)|  _____)| | ____ | |")
    print("| (         | |   | (\ (         ) |   | |     | (      | (   ) || | \   |   | |   | (   ) |      ) |   ) (     | (\ (   | (      | | \_  )(_)")
    print("| )      ___) (___| ) \ \__/\____) |   | |     | )      | )   ( || )  \  |   | |   | )   ( |/\____) |   | |     | ) \ \__| )      | (___) | _ ")
    print("|/       \_______/|/   \__/\_______)   )_(     |/       |/     \||/    )_)   )_(   |/     \|\_______)   \_/     |/   \__/|/       (_______)(_)")
    input("\nPress ENTER to begin game.")

def universal_menu(prompt, options):
    """
    Displays a menu with the given options and prompts the user for a selection.

    Args:
        prompt (str): The prompt to display before the menu options.
        options (list): A list of menu option strings.

    Returns:
        int: The index (1-based) of the selected option.
    """
    while True:
        clear_screen()
        print(prompt)
        for i, option in enumerate(options, 1):
            print(f"  {i}. {option}")

        choice = input("\nEnter your choice: ").strip()

        if choice.isdigit():
            choice = int(choice)
            if 1 <= choice <= len(options):
                return choice
        print("Invalid selection. Please try again.")
        input("Press ENTER to continue...")

# Old character management menu
"""
def display_menu():
    clear_screen()
    print("Welcome to the Character Management System!\n")
    print("  1. Create character")
    print("  2. Display character")
    print("  3. Update character name")
    print("  4. Save character")
    print("  5. Load character")
    print("  6. Exit to Main Menu")

# Function to run the main menu
def run_menu():
    global current_character
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == "1":
            player_character.create_character()
        elif choice == "2":
            player_character.display_character()
        elif choice == "3":
            player_character.update_character()
        elif choice == "4":
            player_character.save_character()
        elif choice == "5":
            player_character.load_character()
        elif choice == "6":
            return
        else:
            print("Invalid choice. Please try again.")

"""
def main_menu():
    prompt = "Select an option from below:\n"
    options = ["Load character", "Create new character", "Start game", "Quit game"]
    selection = universal_menu(prompt, options)
    if selection == 1:
        player_character.load_character()
    elif selection == 2:
        player_character.create_character()
    elif selection == 3:
        if current_character["player"] == "":
            clear_screen()
            print("Please load or create a character.\n")
            print("Returning to main menu...")
            time.sleep(2)
            main_menu()
        game_menu()
    elif selection == 4:
        clear_screen()
        print("Exiting game...\n")
        time.sleep(1)
        clear_screen()
        print("Exiting game..\n")
        time.sleep(1)
        clear_screen()
        print("Exiting game.\n")
        time.sleep(1)
        clear_screen()
        print("Thanks for playing!\n")
        sys.exit()
    main_menu()

def game_menu():
    prompt = "Select an option from below:\n"
    options = ["View character", "Enter town", "Exit to Main Menu"]
    print("Game Menu:")
    selection = universal_menu(prompt, options)
    if selection == 1:
        player_character.display_character()
        game_menu()
    elif selection == 2:
        pass
    elif selection == 3:
        main_menu()

def main():
    welcome_screen()
    main_menu()

    # if choice == "1":
    #     run_menu()
    #     main()
    # elif choice == "2":
    #     start_game()
    # elif choice == "3":
    #     print("Exiting game...")
    #     time.sleep(1)
    #     clear_screen()
    # else:
    #     print("Invalid choice. Please try again.")
    #     time.sleep(1)
    #     main()
    # return






main()