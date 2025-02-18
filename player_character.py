# Player character management

# Load required libraries
import os

# Global variables
main_character ={"player": "", "character": "", "class": "", "level": 1, "max_hp": 100, "current_hp": 100, "max_stamina": 100, "current_stamina": 100, "max_mana": 100, "current_mana": 100, "physical": 1, "mental": 1, "social": 1, "skills": {}}  # Dictionary to store character data
warrior_stats = {"player": "", "character": "", "class": "Warrior", "level": 1, "max_hp": 120, "current_hp": 120, "max_stamina": 120, "current_stamina": 120, "max_mana": 80, "current_mana": 80, "physical": 3, "mental": 1, "social": 1, "skills": {"Sword Slash": 1, "Shield Block": 1}}  # Dictionary to store warrior stats
mage_stats = {"player": "", "character": "", "class": "Mage", "level": 1, "max_hp": 80, "current_hp": 80, "max_stamina": 80, "current_stamina": 80, "max_mana": 120, "current_mana": 120, "physical": 1, "mental": 3, "social": 1, "skills": {"Burning Hands": 1, "Decipher Script": 1}}  # Dictionary to store mage stats
rogue_stats = {"player": "", "character": "", "class": "Rogue", "level": 1, "max_hp": 100, "max_stamina": 100, "max_mana": 100, "physical": 2, "mental": 1, "social": 2, "skills": {"Stealth": 1, "Pick Lock": 1}}  # Dictionary to store rogue stats
cleric_stats = {"player": "", "character": "", "class": "Cleric", "level": 1, "max_hp": 100, "max_stamina": 100, "max_mana": 100, "physical": 1, "mental": 2, "social": 2, "skills": {"Heal": 1, "Persuade": 1}}  # Dictionary to store cleric stats

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    return

# Function to define classes
def character_classes():
    return ["Warrior", "Mage", "Rogue", "Cleric"]

# Function to create a new character
def create_character():
    clear_screen()
    global main_character
    print("Creating a new character...")
    player_name = input("Enter your name: ")
    character_name = input("Enter your character's name: ")
    #main_character["class"] = input("Choose your character's class: ")
    while True:
        try:
            choice = int(input("Choose your character's class:\n1. Warrior\n2. Mage\n3. Rogue\n4. Cleric\nEnter your choice: "))
            if choice == 1:
                main_character = warrior_stats.copy()
                break
            elif choice == 2:
                main_character = mage_stats.copy()
                break
            elif choice == 3:
                main_character = rogue_stats.copy()
                break
            elif choice == 4:
                main_character = cleric_stats.copy()
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid choice. Please try again.")
    main_character["player"] = player_name
    main_character["character"] = character_name
    print(main_character)
    print("Character created successfully!")
    input("Press any key to return to main menu.")
    return

# Function to display character information
def display_character():
    clear_screen()
    if main_character["player"] == "":
        print("No character found. Please create a new character.")
        input("Press any key to return to main menu.")
        return
    print("Displaying character...")
    print("Player: " + main_character["player"])
    print("Character: " + main_character["character"])
    print("Class: " + main_character["class"])
    print("Level: " + str(main_character["level"]))
    print("Max HP: " + str(main_character["max_hp"]))
    print("Current HP: " + str(main_character["current_hp"]))
    print("Max Stamina: " + str(main_character["max_stamina"]))
    print("Current Stamina: " + str(main_character["current_stamina"]))
    print("Max Mana: " + str(main_character["max_mana"]))
    print("Current Mana: " + str(main_character["current_mana"]))
    print("Physical: " + str(main_character["physical"]))
    print("Mental: " + str(main_character["mental"]))
    print("Social: " + str(main_character["social"]))
    print("Skills: " + str(main_character["skills"]))
    input("Press any key to return to main menu.")
    return

# Function to update character information
def update_character():
    clear_screen()
    print("Updating character...")
    main_character["player"] = input("Enter your name: ")
    main_character["character"] = input("Enter your character's name: ")
    main_character["class"] = input("Enter your character's class: ")
    print("Character updated successfully!")
    input("Press any key to return to main menu.")
    return

# Function to delete character information
def delete_character():
    clear_screen()
    print("Deleting character...")
    main_character["player"] = ""
    main_character["character"] = ""
    main_character["class"] = ""
    main_character["level"] = 1
    main_character["max_hp"] = 100
    main_character["current_hp"] = 100
    main_character["max_stamina"] = 100
    main_character["current_stamina"] = 100
    main_character["max_mana"] = 100
    main_character["current_mana"] = 100
    main_character["physical"] = 1
    main_character["mental"] = 1
    main_character["social"] = 1
    main_character["skills"] = {}
    print("Character deleted successfully!")
    input("Press any key to return to main menu.")
    return

# Function to save character information
def save_character():
    clear_screen()
    print("Saving character...")
    with open("character.txt", "w") as file:
        file.write(str(main_character))
    print("Character saved successfully!")
    input("Press any key to return to main menu.")
    return

# Function to load character information
def load_character():
    clear_screen()
    print("Loading character...")
    global main_character
    with open("character.txt", "r") as file:
        main_character = eval(file.read())
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
    print("  4. Delete character")
    print("  5. Save character")
    print("  6. Load character")
    print("  7. Exit")

# Function to run the main menu
def run_menu():
    while True:
        display_menu()
        choice = input("\nEnter your choice: ")
        if choice == "1":
            create_character()
        elif choice == "2":
            display_character()
        elif choice == "3":
            update_character()
        elif choice == "4":
            delete_character()
        elif choice == "5":
            save_character()
        elif choice == "6":
            load_character()
        elif choice == "7":
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

