# Combat resolution system for the game

# Import libraries
import os
import random
# import player_character

# Global variables
# Player
player_character = {"player": "Test", "character": "Hero", "class": "Warrior", "level": 1, "max_hp": 120, "current_hp": 120, "max_stamina": 120, "current_stamina": 120, "max_mana": 80, "current_mana": 80, "physical": 3, "mental": 1, "social": 1, "attack_skill": 1, "skills": {"Sword Slash": 1, "Shield Block": 1}, "Equipped Weapon": ("Short Sword", 1)}


test_character = {"max_hp": 100, "current_hp": 100, "physical": 3, "combat_skill": 1, "weapon_modifier": 1, "armor_modifier": 1}
test_enemy = {"max_hp": 50, "current_hp": 50, "physical": 2, "combat_skill": 1, "weapon_modifier": 1, "armor_modifier": 1}

# Physical Attack = Physical + Combat Skill * Weapon Modifier
# Magic Attack = Mental + Magic Skill * Spell Modifier
# Social Attack = Social + Charm Skill
# Physical Defense = Combat Skill + Armor Modifier
# Magic Defense = Magic Skill + Spell Resistance
# Social Defense = Social Skill + Charm Resistance

# Enemy
enemy_creature = {"creature_name": "", "creature_type": "", "challenge_rating": 1, "max_hp": 100, "current_hp": 100, "max_mana": 100, "current_mana": 100, "physical": 1, "mental": 1, "social": 1, "skills": {}}
orc1 = {"creature_name": "Orc 1", "creature_type": "orc", "challenge_rating": 1, "max_hp": 50, "current_hp": 50, "max_mana": 0, "current_mana": 0, "physical": 2, "mental": 1, "social": 1, "skills": {"Club Bash": 1}, "weapon": {"Club", 1}}

# Function to resolve combat
def combat(attacker, defender):
    attack = calculate_attack(attacker)
    defense = calculate_defense(defender)
    return attack - defense

# Function to calculate attack
def calculate_attack(attacker):
    return attacker["physical"] + attacker["combat_skill"] * attacker["weapon_modifier"]

# Function to calculate defense
def calculate_defense(defender):
    return defender["combat_skill"] + defender["armor_modifier"]

print(f" Hero hits creature for: {combat(test_character, test_enemy)} damage!")