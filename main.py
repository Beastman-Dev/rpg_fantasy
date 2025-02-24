# Text-based fantasy rpg game

# Load libraries
import os
import sys
import time
import player_character
import combat_system
import quest_manager
import town_manager
import pyfiglet

# Define global variables
current_character = player_character.current_character
current_location = {}

# Function for clearing the screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    return

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

def main_menu():
    global current_character
    prompt = "Main Menu:\n \nSelect an option from below:\n"
    options = ["Load character", "Create new character", "View character", "Start game", "Quit game"]
    selection = universal_menu(prompt, options)
    if selection == 1:
        current_character = player_character.load_character()
    elif selection == 2:
        current_character = player_character.create_character()
    elif selection == 3:
        player_character.display_character()
    elif selection == 4:
        if current_character["player"] == "":
            clear_screen()
            print("Please load or create a character.\n")
            print("Returning to main menu...\n")
            time.sleep(1)
            main_menu()
        #input()
        print("\n   Loading game menu...\n")
        time.sleep(1)
        game_menu()
    elif selection == 5:
        clear_screen()
        print("Exiting game...\n")
        time.sleep(1)
        clear_screen()
        print("Thanks for playing!\n")
        sys.exit()
    main_menu()

def game_menu():
    prompt = "Game Menu:\n \nSelect an option from below:\n"
    options = ["View character", "Enter town", "Exit to Main Menu"]
    selection = universal_menu(prompt, options)
    if selection == 1:
        player_character.display_character()
        game_menu()
    elif selection == 2:
        display_town()
    elif selection == 3:
        main_menu()

def display_town():
    prompt = "Town Menu:\nChoose a location to visit or enter '0' for Main Menu...\n"
    options = town_manager.list_town_locations()
    options.append("Quit to Main Menu")
    selection = universal_menu(prompt, options)
    if selection == 1:
        print(f"You selected the {options[0]}")
        inn_prompt = town_manager.town_locations["Inn"]["Greeting"]
        inn_options = town_manager.town_locations["Inn"]["Services"]
        print(inn_prompt)
        print(inn_options)
        service_selection = universal_menu(inn_prompt, inn_options)
        if service_selection == 1:
            print(f"You have chosen {inn_options[0]}.")
        elif service_selection == 2:
            print(f"You have chosen {inn_options[1]}.")
        elif service_selection == 3:
            print(f"You have chosen {inn_options[2]}.")
        print("This location is under construction. Please check back later.")
        input("Press any key to return to Town Menu...")
        display_town()
    elif selection == 2:
        print(f"You selected the {options[1]}")
        blacksmith_prompt = town_manager.town_locations["Blacksmith"]["Greeting"]
        blacksmith_options = town_manager.town_locations["Blacksmith"]["Services"]
        print(blacksmith_prompt)
        print(blacksmith_options)
        service_selection = universal_menu(blacksmith_prompt, blacksmith_options)
        if service_selection == 1:
            print(f"You have chosen {blacksmith_options[0]}.")
        elif service_selection == 2:
            print(f"You have chosen {blacksmith_options[1]}.")
        elif service_selection == 3:
            print(f"You have chosen {blacksmith_options[2]}.")
        print("This location is under construction. Please check back later.")
        input("Press any key to return to Town Menu...")
        display_town()
    elif selection == 3:
        print(f"You selected the {options[2]}")
        alchemist_prompt = town_manager.town_locations["Alchemist"]["Greeting"]
        alchemist_options = town_manager.town_locations["Alchemist"]["Services"]
        print(alchemist_prompt)
        print(alchemist_options)
        service_selection = universal_menu(alchemist_prompt, alchemist_options)
        if service_selection == 1:
            print(f"You have chosen {alchemist_options[0]}.")
        elif service_selection == 2:
            print(f"You have chosen {alchemist_options[1]}.")
        elif service_selection == 3:
            print(f"You have chosen {alchemist_options[2]}.")
        print("This location is under construction. Please check back later.")
        input("Press any key to return to Town Menu...")
        display_town()
    elif selection == 4:
        print(f"You selected the {options[3]}")
        cleric_prompt = town_manager.town_locations["Cleric"]["Greeting"]
        cleric_options = town_manager.town_locations["Cleric"]["Services"]
        print(cleric_prompt)
        print(cleric_options)
        service_selection = universal_menu(cleric_prompt, cleric_options)
        if service_selection == 1:
            print(f"You have chosen {cleric_options[0]}.")
        elif service_selection == 2:
            print(f"You have chosen {cleric_options[1]}.")
        elif service_selection == 3:
            print(f"You have chosen {cleric_options[2]}.")
        print("This location is under construction. Please check back later.")
        input("Press any key to return to Town Menu...")
        display_town()
    elif selection == 5:
        print(f"You selected the {options[4]}")
        general_store_prompt = town_manager.town_locations["General Store"]["Greeting"]
        general_store_options = town_manager.town_locations["General Store"]["Services"]
        print(general_store_prompt)
        print(general_store_options)
        service_selection = universal_menu(general_store_prompt, general_store_options)
        if service_selection == 1:
            print(f"You have chosen {general_store_options[0]}.")
        elif service_selection == 2:
            print(f"You have chosen {general_store_options[1]}.")
        elif service_selection == 3:
            print(f"You have chosen {general_store_options[2]}.")
        print("This location is under construction. Please check back later.")
        input("Press any key to return to Town Menu...")
        display_town()
    elif selection == 6:
        clear_screen()
        print("Returning to Main Menu...\n")
        time.sleep(2)
        main_menu()
    else:
        print("Invalid selection - try again...")
        time.sleep(2)
        display_town()

def main():
    clear_screen()
    print("Welcome to...\n")
    print(pyfiglet.figlet_format("First Fantasy RPG", font="standard"))
    print("By Beastman-Dev!\n")
    input("   Press any key to continue")
    main_menu()

main()