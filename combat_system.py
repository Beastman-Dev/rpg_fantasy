# Combat resolution system for the game

# Import libraries
import os
import random
# import player_character

# Global variables
# Player
player_character = {
    "player": "Test", 
    "name": "Hero", 
    "class": "Warrior", 
    "level": 1, 
    "max_hp": 120, 
    "current_hp": 120, 
    "max_stamina": 120, 
    "current_stamina": 120, 
    "max_mana": 80, 
    "current_mana": 80, 
    "physical": 3, 
    "mental": 1, 
    "social": 1, 
    "combat_skill": 1, 
    "magic_skill": 0,
    "charm_skill": 0,
    "weapon_modifier": 1,
    "spell_modifier": 1,
    "social_modifier": 1,
    "physical_resistance": 1,
    "magic_resistance": 0,
    "charm_resistance": 0,
    "skills": {
        "Sword Slash": 1, 
        "Shield Block": 1
    }, 
    "Equipped Weapon": ("Short Sword", 1)
    }

enemy_creature = {
    "name": "Goblin",
    "type": "Humanoid",
    "challenge_rating": 1,
    "max_hp": 50, 
    "current_hp": 50, 
    "max_mana": 50, 
    "current_mana": 50, 
    "physical": 2, 
    "mental": 1,
    "social": 1,
    "combat_skill": 1,
    "magic_skill": 0,
    "charm_skill": 0,
    "weapon_modifier": 1, 
    "spell_modifier": 1,
    "social_modifier": 1,
    "physical_resistance": 1,
    "magic_resistance": 0,
    "charm_resistance": 0
    }

# Physical Attack = Physical + Combat Skill * Weapon Modifier
# Magic Attack = Mental + Magic Skill * Spell Modifier
# Social Attack = Social + Charm Skill * Social Modifier
# Physical Defense = Combat Skill + Physical Resistance
# Magic Defense = Magic Skill + Magic Resistance
# Social Defense = Social Skill + Charm Resistance


# Function to resolve combat
def weapon_combat(attacker, defender):
    attack = attacker["physical"] + attacker["combat_skill"] * attacker["weapon_modifier"]
    defense = defender["combat_skill"] + defender["physical_resistance"]
    return attack - defense

def magic_combat(attacker, defender):
    attack = attacker["mental"] + attacker["magic_skill"] * attacker["spell_modifier"]
    defense = defender["magic_skill"] + defender["magic_resistance"]
    return attack - defense

def social_combat(attacker, defender):
    attack = attacker["social"] + attacker["charm_skill"] * attacker["social_modifier"]
    defense = defender["charm_skill"] + defender["charm_resistance"]
    return attack - defense

def combat_round(attacker, defender):
    print(attacker["name"] + " attacks " + defender["name"] + "!")
    attack_type = 1
    if attack_type == 1:
        damage = weapon_combat(attacker, defender)
        print("Physical attack!")
    elif attack_type == 2:
        damage = magic_combat(attacker, defender)
        print("Magic attack!")
    else:
        damage = social_combat(attacker, defender)
        print("Social attack!")
    if damage > 0:
        print("Hit for " + str(damage) + " damage!")
        defender["current_hp"] -= damage
    else:
        print("Miss!")
    if defender["current_hp"] <= 0:
        print(defender["name"] + " has been defeated!")
        return True
    return False

def combat_system():
    global player_character
    global enemy_creature
    clear_screen()
    print("Combat system")
    print("Character: " + player_character["name"])
    print("Class: " + player_character["class"])
    print("Level: " + str(player_character["level"]))
    print("HP: " + str(player_character["current_hp"]) + "/" + str(player_character["max_hp"]))
    print("Mana: " + str(player_character["current_mana"]) + "/" + str(player_character["max_mana"]))
    print("Physical: " + str(player_character["physical"]))
    print("Mental: " + str(player_character["mental"]))
    print("Social: " + str(player_character["social"]))
    print("Skills: " + str(player_character["skills"]))
    print("\nvs.")
    print("Creature: " + enemy_creature["name"])
    print("Type: " + enemy_creature["type"])
    print("Challenge rating: " + str(enemy_creature["challenge_rating"]))
    print("HP: " + str(enemy_creature["current_hp"]) + "/" + str(enemy_creature["max_hp"]))
    print("Mana: " + str(enemy_creature["current_mana"]) + "/" + str(enemy_creature["max_mana"]))
    print("Physical: " + str(enemy_creature["physical"]))
    print("Mental: " + str(enemy_creature["mental"]))
    print("Social: " + str(enemy_creature["social"]))
    input("\nPress any key to start combat...")
    while True:
        if combat_round(player_character, enemy_creature):
            break
        if combat_round(enemy_creature, player_character):
            break
    input("Press any key to return to main menu.")
    return

# Function to clear the screen
def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    return

# Main program
if __name__ == "__main__":
    combat_system()
    clear_screen()
    print("Exiting combat system...")
    input("Press any key to continue...")
    clear_screen()
    print("Returning to main menu...")
    input("Press any key to exit...")
    clear_screen()
    print("Goodbye!")
    exit()

