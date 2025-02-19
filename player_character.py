# Player character management

# Load required libraries
import os

# Global variables
main_character ={
    "player": "", 
    "name": "", 
    "class": "", 
    "level": 1, 
    "max_hp": 0, 
    "current_hp": 0, 
    "max_stamina": 0, 
    "current_stamina": 0, 
    "max_mana": 0, 
    "current_mana": 0, 
    "physical": 0, 
    "mental": 0, 
    "social": 0, 
    "combat_skill": 0,
    "magic_skill": 0,
    "charm_skill": 0,
    "weapon_modifier": 0,
    "spell_modifier": 0,
    "social_modifier": 0,
    "physical_resistance": 0,
    "magic_resistance": 0,
    "charm_resistance": 0,
    "skills": {}, 
    "equipped_weapon": ("", 0),
    "equipped_armor": ("", 0),
    "equipped_shield": ("", 0),
    "equipped_spell": ("", 0),
    "spells": {},
    "inventory": {}
    }  # Dictionary to store character data
current_character = main_character.copy()  # Dictionary to store current character data

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

    print("Character created successfully!")
    input("Press any key to return to main menu.")
    return current_character

# Function to display character information
def display_character():
    global current_character
    clear_screen()
    if current_character["player"] == "":
        print("No character found. Please create a new character.")
        input("Press any key to return to main menu.")
        return
    print("Displaying character...")
    print(f"Player: {current_character["player"]}")
    print(f"Character: {current_character["name"]}")
    print(f"Class: {current_character["class"]}")
    print(f"Level: {str(current_character["level"])}")
    print(f"HP: {current_character["current_hp"]}/{current_character["max_hp"]}")
    print(f"Stamina: {current_character["current_stamina"]}/{current_character["max_stamina"]}")
    print(f"Mana: {current_character["current_mana"]}/{current_character["max_mana"]}")
    print(f"Physical: {current_character["physical"]}  Mental: {current_character["mental"]}  Social: {current_character["social"]}")
    print(f"Skills: {current_character["skills"]}")
    input("Press any key to return to main menu.")
    return

# Function to update character information
def update_character():
    clear_screen()
    print("Updating character name...")
    current_character["name"] = input("Enter your character's name: ")
    print("Character updated successfully!")
    input("Press any key to return to main menu.")

# Function to save character information
def save_character():
    clear_screen()
    print("Saving character...")
    with open("character.txt", "w") as file:
        file.write(str(current_character))
    print("Character saved successfully!")
    input("Press any key to return to main menu.")
    return

# Function to load character information
def load_character():
    clear_screen()
    global current_character
    if current_character["player"] != "":
        print("Character already exists. Do you want to overwrite it?")
        choice = input("Enter 'Y' to overwrite or 'N' to cancel: ")
        if choice.upper() != "Y":
            print("Load character cancelled.")
            input("Press any key to return to main menu.")
            return
    print("Loading character...")
    with open("character.txt", "r") as file:
        current_character = eval(file.read())
    print("Character loaded successfully!")
    input("Press any key to return to main menu.")
    return

# Function to display the main menu
def display_menu():
    clear_screen()
    print("Welcome to the Player Character Management System!\n")
    print("  1. Create character")
    print("  2. Display character")
    print("  3. Update character")
    print("  4. Save character")
    print("  5. Load character")
    print("  6. Exit")

# Function to run the main menu
def run_menu():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == "1":
            current_character = create_character()
        elif choice == "2":
            display_character()
        elif choice == "3":
            update_character()
        elif choice == "4":
            save_character()
        elif choice == "5":
            load_character()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

# Main function
def main():
    run_menu()

# Entry point of the program
if __name__ == "__main__":
    main()

# End of program

