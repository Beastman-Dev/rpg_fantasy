# Text-based fantasy rpg game

import os
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
    print(f"\nMain Menu\n")
    print("  1. Character Menu")
    print("  2. Start Game")
    print("  3. Exit")
    choice = input("\nEnter your choice: ")
    return choice

# def start_game():
#     clear_screen()
#     print("Starting game...")
#     time.sleep(1)
#     main()



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