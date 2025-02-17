# Text-based fantasy rpg game

import os
import time

# Define global variables for character data
player_character = {"player": "", "character": ""}
character_class = {"class": "", "level": 1}
character_hp = {"max": 100, "current": 100}
character_stamina = {"max": 100, "current": 100}
character_mana = {"max": 100, "current": 100}
character_stats = {"physical": 1, "mental": 1, "social": 1}
character_skills = {}

# Define global variables for game text
welcome_text = "Welcome to First Fantasy RPG!"
character_creation_text = "Let's create your character."

# Define global variables for system information
folder_path = "~/workspace/github.com/Beastman-Dev/rpg_fantasy/saves"
filename = "character_save"
save_slot = 0

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    return

def create_character():
    clear_screen()
    player_character["player"] = input("What is your name? ")
    clear_screen()
    print(f"Hello, {player_character["player"]}!\n")
    print("Let's create your character.\n")
    player_character["character"] = input("What is your character's name? ")
    clear_screen()
    print("Great! Your character's name is " + player_character["character"] + ".")
    print("Now, let's choose your character's class.")
    # print("Choose from the following classes:")
    print("1. Warrior")
    print("2. Mage")
    print("3. Rogue")
    print("4. Cleric")
    class_choice = input("What class would you like to be? ")
    clear_screen()
    if class_choice == "1":
        character_class["class"] = "Warrior"
        character_stats["physical"] = 3
        character_skills["Sword Slash"] = 1
        character_skills["Shield Block"] = 1
    elif class_choice == "2":
        character_class["class"] = "Mage"
        character_stats["mental"] = 3
        character_skills["Burning Hands"] = 1
        character_skills["Decipher Script"] = 1
    elif class_choice == "3":
        character_class["class"] = "Rogue"
        character_stats["physical"] = 2
        character_stats["social"] = 2
        character_skills["Stealth"] = 1
        character_skills["Pick Lock"] = 1
    elif class_choice == "4":
        character_class["class"] = "Cleric"
        character_stats["mental"] = 2
        character_stats["social"] = 2
        character_skills["Heal"] = 1
        character_skills["Persuade"] = 1
    else:
        print("Invalid choice. Please try again.")
        time.sleep(5)
        create_character()
    print(f"{player_character["character"]}, level {character_class["level"]} {character_class["class"]}.")
    print(f"Physical: {character_stats["physical"]}  Mental: {character_stats["mental"]}  Social: {character_stats["social"]}")
    if character_class["class"] == "Mage" or character_class["class"] == "Cleric":
        print(f"HP: {character_hp["current"]}/{character_hp["max"]}  Stamina: {character_stamina["current"]}/{character_stamina["max"]}  Mana: {character_mana["current"]}/{character_mana["max"]}")
    else:
        print(f"HP: {character_hp["current"]}/{character_hp["max"]}  Stamina: {character_stamina["current"]}/{character_stamina["max"]}")
    print("Skills:")
    for skill in character_skills:
        print(f" > {skill} {character_skills[skill]}")

    print(f"\n1. Save character data\n2. Return to main menu")
    choice = input("Enter your choice: ")
    if choice == "1":
        save_data_manager(folder_path, filename)
    elif choice == "2":
        main()

def save_data_manager(folder_path, filename):
    clear_screen()
    # Check for existing save files
    existing_saves = []
    for i in range(1, 6): # Assuming 5 save slots
        file_path = os.path.join(folder_path, f"{filename}_slot{i}.dat")
        if os.path.exists(file_path):
            existing_saves.append(i)

    # Display existing save slots
    print("Existing save slots:")
    if existing_saves:
        for slot in existing_saves:
            print(f"Slot {slot}")
    else:
        print("No existing save slots found.")
    
    # Prompt user to save or load character
    print("\n1. Load character\n2. Save character\n3. Return to main menu")
    choice = input("Enter your choice: ")

    if choice == "1":
        if not existing_saves:
            print("No existing character data found.")
            print("Press any key to return to main menu.")
            input()
            main()
        else:
            print("Enter the save slot number to load:")
            save_slot = int(input("Enter save slot: "))
            load_character_data(folder_path, filename, save_slot)
    elif choice == "2":
        save_slot = input("Enter the save slot number to save: ").strip()

        try:
            save_slot = int(save_slot)
            if 1 <= save_slot <= 5:  # Assuming 5 save slots
                save_character_data(folder_path, filename, save_slot)
            else:
                print("Invalid save slot. Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input. Please enter a number.")
    elif choice == "3":
        print("Returning to main menu.")
        main()

    else:
        print("Invalid choice. Please try again.")
        save_data_manager(folder_path, filename)

def save_character_data(folder_path, filename, save_slot):
    """Saves global character-related data to a text file in a structured format."""
    global player_character, character_class, character_hp, character_stamina
    global character_mana, character_stats, character_skills

    # Create the folder if it doesn't exist
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    # Modify the filename to include the save slot
    file_path = os.path.join(folder_path, f"{filename}_slot{save_slot}.dat")

    try:
        with open(file_path, "w") as file:
            file.write(f"[Save Slot {save_slot}]\n")

            file.write("\n[Player Character]\n")
            for key, value in player_character.items():
                file.write(f"{key}: {value}\n")

            file.write("\n[Character Class]\n")
            for key, value in character_class.items():
                file.write(f"{key}: {value}\n")

            file.write("\n[Character HP]\n")
            for key, value in character_hp.items():
                file.write(f"{key}: {value}\n")

            file.write("\n[Character Stamina]\n")
            for key, value in character_stamina.items():
                file.write(f"{key}: {value}\n")

            file.write("\n[Character Mana]\n")
            for key, value in character_mana.items():
                file.write(f"{key}: {value}\n")

            file.write("\n[Character Stats]\n")
            for key, value in character_stats.items():
                file.write(f"{key}: {value}\n")

            file.write("\n[Character Skills]\n")
            if character_skills:
                for skill, level in character_skills.items():
                    file.write(f"{skill}: {level}\n")
            else:
                file.write("None\n")  # Indicate no skills if dictionary is empty
        
        print(f"Character data saved to {file_path}")
    except Exception as e:
        print(f"Error saving character data: {e}")

    print("Press any key to return to main menu.")
    input()
    main()

def load_character_data(folder_path, filename, save_slot):
    """Loads character-related data from a text file and updates global variables."""
    global player_character, character_class, character_hp, character_stamina
    global character_mana, character_stats, character_skills

    # Construct the file path with the save slot
    file_path = os.path.join(folder_path, f"{filename}_slot{save_slot}.dat")

    try:
        with open(file_path, "r") as file:
            section = None  # Track which section we are currently reading

            for line in file:
                line = line.strip()
                if not line:
                    continue  # Skip empty lines
                
                # Identify sections
                if line.startswith("[") and line.endswith("]"):
                    section = line.strip("[]")
                    continue

                # Process key-value pairs
                if ":" in line:
                    key, value = line.split(":", 1)
                    key, value = key.strip(), value.strip()

                    # Convert numerical values to integers if possible
                    # if value.isdigit():
                    #    value = int(value)

                    # Assign values to the correct section
                    if section == "Player Character":
                        player_character[key] = value
                    elif section == "Character Class":
                        character_class[key] = value
                    elif section == "Character HP":
                        character_hp[key] = value
                    elif section == "Character Stamina":
                        character_stamina[key] = value
                    elif section == "Character Mana":
                        character_mana[key] = value
                    elif section == "Character Stats":
                        character_stats[key] = value
                    elif section == "Character Skills":
                        if value.isdigit():
                            character_skills[key] = int(value)
                        else:
                            character_skills[key] = value  # If skills are stored differently

        print(f"Character data loaded from {file_path}")

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
    except Exception as e:
        print(f"Error loading character data: {e}")

    print("Press any key to return to main menu.")
    input()
    main()

def view_character_data():
    print("Player Character:")
    for key, value in player_character.items():
        print(f"  {key}: {value}")

    print("\nCharacter Class:")
    for key, value in character_class.items():
        print(f"  {key}: {value}")

    print("\nCharacter HP:")
    for key, value in character_hp.items():
        print(f"  {key}: {value}")

    print("\nCharacter Stamina:")
    for key, value in character_stamina.items():
        print(f"  {key}: {value}")

    print("\nCharacter Mana:")
    for key, value in character_mana.items():
        print(f"  {key}: {value}")

    print("\nCharacter Stats:")
    for key, value in character_stats.items():
        print(f"  {key}: {value}")

    print("\nCharacter Skills:")
    for skill, level in character_skills.items():
        print(f"  {skill}: {level}")

    print()

    print("Press any key to return to main menu.")
    input()
    main()

def main():
    clear_screen()
    print(f"{welcome_text}\n")
    print("What would you like to do?\n")
    print("1. Create a new character")
    print("2. Load an existing character")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == "00":
        print("Debug - view character data")
        clear_screen()
        view_character_data()
    elif choice == "1":
        clear_screen()
        create_character()
    elif choice == "2":
        clear_screen()
        save_data_manager(folder_path, filename)
    elif choice == "3":
        print("Goodbye!")
        exit()
    else:
        print("Invalid choice. Please try again.")


main()