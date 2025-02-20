# Quest manager

# Quests
# Quests are the main way to progress in the game. They are given by NPCs and can be completed in a variety of ways. Quests can be completed by defeating enemies, gathering items, or completing tasks. Quests can also have multiple stages and rewards. Quests are stored in a dictionary with the following format:
# {Quest(quest_name, quest_description, quest_type, quest_difficulty, quest_rewards, quest_requirements, quest_stages)}
quest_name = "Lost Puppy"
quest_description = "Find the lost puppy and return it to its owner."
quest_type = "Fetch"
quest_difficulty = 1
quest_rewards = {"Gold": 10, "XP": 5}
quest_requirements = {"Level": 1}
quest_stages = ["Find the lost puppy", "Return the lost puppy to its owner"]
quest = Quest(quest_name, quest_description, quest_type, quest_difficulty, quest_rewards, quest_requirements, quest_stages)
quests = {"Lost Puppy": quest}
