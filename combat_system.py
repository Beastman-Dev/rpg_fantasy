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

