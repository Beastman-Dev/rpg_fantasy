# Combat resolution system for the game

# Import the random module
import random
# import player_character

# Enemy
enemy_creature = {"creature_name": "", "creature_type": "", "challenge_rating": 1, "max_hp": 100, "current_hp": 100, "max_mana": 100, "current_mana": 100, "physical": 1, "mental": 1, "social": 1, "skills": {}}
orc1 = {"creature_name": "Orc 1", "creature_type": "orc", "challenge_rating": 1, "max_hp": 50, "current_hp": 50, "max_mana": 0, "current_mana": 0, "physical": 2, "mental": 1, "social": 1, "skills": {"Club Bash": 1}, "weapon": {"Club", 1}}

# Function to resolve combat
# print(player_character)
enemy_skills = orc1["skills"]
enemy_attack = random.choice(list(enemy_skills.keys()))
print(enemy_attack)