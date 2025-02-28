# Player character management

# Load required libraries
import os
import ast
from config import *

# Function to clear the screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    return

# Function to create a warrior character
def create_warrior():
    current_character["class"] = "Warrior"
    current_character["max_hp"] = 120
    current_character["current_hp"] = 120
    current_character["max_stamina"] = 120
    current_character["current_stamina"] = 120
    current_character["max_mana"] = 80
    current_character["current_mana"] = 80
    current_character["physical"] = 3
    current_character["mental"] = 1
    current_character["social"] = 1
    current_character["combat_skill"] = 1
    current_character["skills"] = {"Sword Slash": 1, "Shield Block": 1}

# Function to create a mage character
def create_mage():
    current_character["class"] = "Mage"
    current_character["max_hp"] = 80
    current_character["current_hp"] = 80
    current_character["max_stamina"] = 80
    current_character["current_stamina"] = 80
    current_character["max_mana"] = 120
    current_character["current_mana"] = 120
    current_character["physical"] = 1
    current_character["mental"] = 3
    current_character["social"] = 1
    current_character["magic_skill"] = 1
    current_character["skills"] = {"Burning Hands": 1, "Decipher Script": 1}

# Function to create a rogue character
def create_rogue():
    current_character["class"] = "Rogue"
    current_character["max_hp"] = 100
    current_character["current_hp"] = 100
    current_character["max_stamina"] = 100
    current_character["current_stamina"] = 100
    current_character["max_mana"] = 100
    current_character["current_mana"] = 100
    current_character["physical"] = 2
    current_character["mental"] = 1
    current_character["social"] = 2
    current_character["charm_skill"] = 1
    current_character["skills"] = {"Stealth": 1, "Pick Lock": 1}

# Function to create a cleric character
def create_cleric():
    current_character["class"] = "Cleric"
    current_character["max_hp"] = 100
    current_character["current_hp"] = 100
    current_character["max_stamina"] = 100
    current_character["current_stamina"] = 100
    current_character["max_mana"] = 100
    current_character["current_mana"] = 100
    current_character["physical"] = 1
    current_character["mental"] = 2
    current_character["social"] = 2
    current_character["charm_skill"] = 1
    current_character["skills"] = {"Heal": 1, "Persuade": 1}

# Function to create a new character
def create_character():
    clear_screen()
    global current_character
    if current_character["player"] != "":
        print("Character already exists. Do you want to overwrite it?")
        choice = input("Enter 'Y' to overwrite or 'N' to cancel: ")
        if choice.upper() != "Y":
            print("Character creation cancelled.")
            input("Press any key to return to main menu.")
            return
    print("Creating a new character...\n")
    current_character["player"] = input("Enter your name: ")
    current_character["name"] = input("Enter your character's name: ")
    while True:
        try:
            choice = int(input("Choose your character's class:\n  1. Warrior\n  2. Mage\n  3. Rogue\n  4. Cleric\nEnter your choice: "))
            if choice == 1:
                create_warrior()
                break
            elif choice == 2:
                create_mage()
                break
            elif choice == 3:
                create_rogue()
                break
            elif choice == 4:
                create_cleric()
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid choice. Please try again.")

    clear_screen()
    print("Character created successfully!\n")
    display_character()
    return current_character

# Function to display character information
def display_character():
    global current_character
    clear_screen()
    if current_character["player"] == "":
        print("Please load or create a character first.\n")
        print("Returning to main menu...\n")
        pause(2)
        return
    print("Displaying character...\n")
    print(f"  Player: {current_character["player"]}")
    print(f"  Character: {current_character["name"]}")
    print(f"  Class: {current_character["class"]}  Level: {str(current_character["level"])}")
    print(f"  HP: {current_character["current_hp"]}/{current_character["max_hp"]}")
    print(f"  Stamina: {current_character["current_stamina"]}/{current_character["max_stamina"]}")
    print(f"  Mana: {current_character["current_mana"]}/{current_character["max_mana"]}")
    print(f"  Physical: {current_character["physical"]}  Mental: {current_character["mental"]}  Social: {current_character["social"]}")
    print(f"  Skills: {current_character["skills"]}")
    input("\nPress any key to return to character menu.")

# Function to update character name
def update_character():
    clear_screen()
    print("Updating character name...")
    current_character["name"] = input("Enter your character's name: ")
    print("Character updated successfully!")
    input("Press any key to return to character menu.")

# Function to save character information
def save_character():
    clear_screen()
    print("Saving character...")
    with open("character.txt", "w") as file:
        file.write(str(current_character))
    print("Character saved successfully!")
    input("Press any key to return to character menu.")
    return

# Function to load character information
def load_character():
    clear_screen()
    global current_character
    if current_character["player"] != "":
        print("Character already exists. Do you want to overwrite it?\n")
        choice = input("Enter 'Y' to overwrite or 'N' to cancel: ")
        if choice.upper() != "Y":
            clear_screen()
            print("Load character cancelled.\n")
            input("Press any key to return to character menu.")
            return
    if os.path.exists("character.txt") == False:
        print("No save file found.\n")
        print("Returning to main menu...\n")
        pause(2)
        return
    clear_screen()
    print("Loading character...\n")
    pause(2)
    with open("character.txt", "r") as file:
        current_character = ast.literal_eval(file.read())
    # with open("character.txt", "r") as file:
    #     current_character = eval(file.read())
    print("  Character loaded successfully!\n")
    pause(2)
    return current_character

# Unit tests

# Unit test for create_character function
#create_character()

# Unit test for display_character function with no player name defined
#display_character()

# Unit test for display_character function with player name assigned
#current_character["player"] = "Bill"
#display_character()

# Unit test for update_character function
update_character()
print(current_character["name"])

# End of player_character.py