# Player character management class

# Global variables
main_character ={"player": "", "character": "", "class": "", "level": 1, "max_hp": 100, "current_hp": 100, "max_stamina": 100, "current_stamina": 100, "max_mana": 100, "current_mana": 100, "physical": 1, "mental": 1, "social": 1, "skills": {}}  # Dictionary to store character data

# Function to create a new character
def create_character():
    print("Creating a new character...")
    main_character["player"] = input("Enter your name: ")
    main_character["character"] = input("Enter your character's name: ")
    main_character["class"] = input("Enter your character's class: ")
    print("Character created successfully!")

# Function to display character information
def display_character():
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

# Function to update character information
def update_character():
    print("Updating character...")
    main_character["player"] = input("Enter your name: ")
    main_character["character"] = input("Enter your character's name: ")
    main_character["class"] = input("Enter your character's class: ")
    print("Character updated successfully!")

# Function to delete character information
def delete_character():
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

# Function to save character information to a file
def save_character():
    print("Saving character...")
    with open("character.txt", "w") as file:
        file.write("Player: " + main_character["player"] + "\n")
        file.write("Character: " + main_character["character"] + "\n")
        file.write("Class: " + main_character["class"] + "\n")
        file.write("Level: " + str(main_character["level"]) + "\n")
        file.write("Max HP: " + str(main_character["max_hp"]) + "\n")
        file.write("Current HP: " + str(main_character["current_hp"]) + "\n")
        file.write("Max Stamina: " + str(main_character["max_stamina"]) + "\n")
        file.write("Current Stamina: " + str(main_character["current_stamina"]) + "\n")
        file.write("Max Mana: " + str(main_character["max_mana"]) + "\n")
        file.write("Current Mana: " + str(main_character["current_mana"]) + "\n")
        file.write("Physical: " + str(main_character["physical"]) + "\n")
        file.write("Mental: " + str(main_character["mental"]) + "\n")
        file.write("Social: " + str(main_character["social"]) + "\n")
        file.write("Skills: " + str(main_character["skills"]) + "\n")
    print("Character saved successfully!")

# Function to load character information from a file
def load_character():
    print("Loading character...")
    with open("character.txt", "r") as file:
        lines = file.readlines()
        main_character["player"] = lines[0].split(": ")[1].strip()
        main_character["character"] = lines[1].split(": ")[1].strip()
        main_character["class"] = lines[2].split(": ")[1].strip()
        main_character["level"] = int(lines[3].split(": ")[1].strip())
        main_character["max_hp"] = int(lines[4].split(": ")[1].strip())
        main_character["current_hp"] = int(lines[5].split(": ")[1].strip())
        main_character["max_stamina"] = int(lines[6].split(": ")[1].strip())
        main_character["current_stamina"] = int(lines[7].split(": ")[1].strip())
        main_character["max_mana"] = int(lines[8].split(": ")[1].strip())
        main_character["current_mana"] = int(lines[9].split(": ")[1].strip())
        main_character["physical"] = int(lines[10].split(": ")[1].strip())
        main_character["mental"] = int(lines[11].split(": ")[1].strip())
        main_character["social"] = int(lines[12].split(": ")[1].strip())
        main_character["skills"] = eval(lines[13].split(": ")[1].strip())
    print("Character loaded successfully!")

# Function to display the main menu
def display_menu():
    print("1. Create character")
    print("2. Display character")
    print("3. Update character")
    print("4. Delete character")
    print("5. Save character")
    print("6. Load character")
    print("7. Exit")

# Function to run the main menu
def run_menu():
    while True:
        display_menu()
        choice = input("Enter your choice: ")
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

