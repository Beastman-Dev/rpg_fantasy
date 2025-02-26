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
current_character = main_character.copy()
current_location = {}
