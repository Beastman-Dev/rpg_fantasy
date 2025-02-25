# Quests are the main way to progress in the game. They are given by NPCs and can be completed in a variety of ways. Quests can be completed by defeating enemies, gathering items, or completing tasks. Quests can also have multiple stages and rewards. Quests are stored in a dictionary with the following format:
# {Quest(quest_name, quest_description, quest_type, quest_difficulty, quest_rewards, quest_requirements, quest_stages)}

import os
import random
import time

# Global variables
quests = {}
GP = 0
XP = 0


# Classes

class Quest:
    def __init__(self, quest_name, quest_description, quest_type, quest_difficulty, quest_rewards, quest_requirements, quest_stages):
        self.quest_name = quest_name
        self.quest_description = quest_description
        self.quest_type = quest_type
        self.quest_difficulty = quest_difficulty
        self.quest_rewards = quest_rewards
        self.quest_requirements = quest_requirements
        self.quest_stages = quest_stages

class QuestManager:
    def __init__(self):
        self.quests = {}

    def add_quest(self, quest):
        self.quests[quest.quest_name] = quest

    def remove_quest(self, quest_name):
        del self.quests[quest_name]

    def get_quest(self, quest_name):
        return self.quests[quest_name]
    
    def get_all_quests(self):
        return
        for quest in self.quests:
            print(quest.quest_name)

# Functions

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    return

# Example quest
def example_quest():
    quest_name = "Lost Puppy"
    quest_description = "Find the lost puppy and return it to its owner."
    quest_type = "Fetch"
    quest_difficulty = 1
    quest_rewards = {"Gold": 10, "XP": 10}
    quest_requirements = {"Level": 1}
    quest_stages = ["Find the lost puppy", "Return the lost puppy to its owner"]
    return quest_name, quest_description, quest_type, quest_difficulty, quest_rewards, quest_requirements, quest_stages

def test_function():
    clear_screen()
    quest = example_quest()
    print(f"Quest Data Input:\n  {quest}")
    print(f"\nQuest Data Breakdown:")
    print(f"  Quest Name: {quest[0]}")
    print(f"  Quest Description: {quest[1]}")
    print(f"  Quest Type: {quest[2]}")
    print(f"  Quest Difficulty: {quest[3]}")
    print(f"  Quest Rewards: {quest[4]}")
    print(f"  Quest Requirements: {quest[5]}")
    print(f"  Quest Stages: {quest[6]}")
    print(f"\nGenerating Quest Record...")
    new_quest = Quest(quest[0], quest[1], quest[2], quest[3], quest[4], quest[5], quest[6])
    print(f"\nAdding Quest Record to Quest Manager...\n")
    quest_manager = QuestManager()
    quest_manager.add_quest(new_quest)
    print(f"Retrieving Quest from Quest Manager...\n")
    print(f"Quest Retrieved from Quest Manager:")
    print(f"  Quest Name: {quest_manager.get_quest("Lost Puppy").quest_name}")
    print(f"  Quest Description: {quest_manager.get_quest("Lost Puppy").quest_description}")
    print(f"  Quest Type: {quest_manager.get_quest("Lost Puppy").quest_type}")
    print(f"  Quest Difficulty: {quest_manager.get_quest("Lost Puppy").quest_difficulty}")
    print(f"  Quest Rewards: {quest_manager.get_quest("Lost Puppy").quest_rewards}")
    print(f"  Quest Requirements: {quest_manager.get_quest("Lost Puppy").quest_requirements}")
    print(f"  Quest Stages: {quest_manager.get_quest("Lost Puppy").quest_stages}")

def enemy_encounter():
    name = ""
    type = "Enemy Encounter"
    difficulty = 0
    enemies = {}
    drops = ""

def obstacle():
    name = ""
    type = "Obstacle"
    difficulty = 0
    test_attribute = ""
    consequence = ""

# Example Enemy Encounters
goblin_solo = {"name": "Lone Goblin", "type": "Enemy Encounter", "difficulty": 1, "enemies": {"goblins": 1}, "drops": (GP, XP)}
goblin_patrol = {"name": "Goblin Patrol", "type": "Enemy Encounter", "difficulty": 2, "enemies": {"goblins": 3}, "drops": (GP, XP)}
goblin_hunting_party = {"name": "Goblin Warband", "type": "Enemy Encounter", "difficulty": 5, "enemies": {"goblins": 5, "goblin champion": 1, "goblin mystic": 1}, "drops": (GP, XP)}
goblin_camp = {"name": "Goblin Camp", "type": "Enemy Encounter", "difficulty": 10, "enemies": {"goblins": 25, "goblin champion": 5, "goblin mystic": 3, "goblin shaman": 1, "goblin chief": 1}, "drops": (GP, XP)}

# Example Obstacles
find_puddles = {"name": "Find Puddles in Woods", "type": "obstacle", "difficulty": 1, "test_attribute": "Mental", "consequences": None, "rewards": None}
thorny_brambles = {"name": "Thorny Brambles", "type": "Obstacle", "difficulty": 1, "test_attribute": "Physical", "consequences": {"HP": -1}, "rewards": None}




# Example Quests
lost_puppy = {"name": "Lost Puppy", "type": "Fetch", "description": "Find the lost puppy and return it to its owner.", "location": "The Foreboding Forest", "stages": ("Find the Lost Puppy", "Rescue the Lost Puppy", "Return the Lost Puppy")}
find_the_lost_puppy = {"turns": 5, "obstacles": {"search": find_puddles, }}

def game_loop(duration, ability, difficulty, success_requirement, failure_limit):
    success_count = 0
    failure_count = 0
    for x in range(duration):
        effort = ability + random.randrange(0,5)
        resistance = difficulty + random.randrange(0,5)
        print(f"Testing... you rolled a {effort} against a difficulty of {resistance}.\n")
        if effort >= resistance:
            print("   You made progress...\n")
            success_count += 1
        else:
            print("   You failed to make progress...\n")
            failure_count += 1
        if success_count >= success_requirement or failure_count >= failure_limit:
            break
    print(f"The challenge took {x + 1} rounds\n")
    if success_count >= success_requirement:
        print("CONGRATULATIONS! You were ultimately successful.\n")
    else:
        print("You ultimately failed. Please try again.\n")


# game_loop(10, 3, 1, 5, 3)

# Variables for the Lost Puppy quest, phase 1 (day)
description_text = "Try to find the dog Puddles before it gets dark outside and the danger increases. You have eight hours and each check requires an hour of time. If you gain three successes you find him. For each two failures, you encounter a goblin patrol. If you fail to locate Puddles before dark, you'll need to decide if you want to continue to search at night. During the night it becomes more difficult to succeed and the goblin patrols are more frequent."
success_text = "You spot some tracks and follow the trail. They are sporadic and hard to discern from the tracks of other animals... and goblins."
failure_text = "The trail goes cold and you continue in the direction you think they were headed, hoping for the best."
darkness_text = "Your heart sinks with the fading sunlight. No luck in finding the missing dog yet, and the trail will be all but impossible to find at night."
decision_text = "With little light left, you're forced to either give up until the morning or light a torch and continue the search into the night. Torchlight will attract enemies and it will be even more difficult to find the trail, if you do."
duration = 8
encounter_frequency = 3
ability = "Mental"
difficulty = 2
