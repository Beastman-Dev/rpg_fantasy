# Quests are the main way to progress in the game. They are given by NPCs and can be completed in a variety of ways. Quests can be completed by defeating enemies, gathering items, or completing tasks. Quests can also have multiple stages and rewards. Quests are stored in a dictionary with the following format:
# {Quest(quest_name, quest_description, quest_type, quest_difficulty, quest_rewards, quest_requirements, quest_stages)}

import os

# Global variables
quests = {}

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