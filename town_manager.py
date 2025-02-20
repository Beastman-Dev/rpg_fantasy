import npc_manager

# Manage town locations and their properties

# Lazy Dragon: Inn and Tavern
# Services: Rest, Gossip, Quests
# Patron: Innkeeper Davrid Havenrest

# Bleeding Edge: Blacksmith
# Services: Buy, Sell, Upgrade
# Patron: Blacksmith Gendry Ironheart

# Leaky Cauldron: Alchemist
# Services: Buy, Sell, Brew
# Patron: Alchemist Elara Moonshadow

# Temple of Light: Cleric
# Services: Heal, Bless, Cure
# Patron: Matron Sylia Lightbringer

# General Goods: General Store
# Services: Buy, Sell, Trade
# Patron: Merchant Tavros Goldleaf

# Specific Town NPCs
Town_NPCs = {
    "Innkeeper Davrid Havenrest": Civilian("Davrid Havenrest", "Innkeeper", 3, 4, 4, 1.5, 2),
    "Blacksmith Gendry Ironheart": Civilian("Gendry Ironheart", "Blacksmith", 3, 2, 2, 1.5, 2),
    "Alchemist Elara Moonshadow": Civilian("Elara Moonshadow", "Alchemist", 4, 3, 3, 1.5, 2),
    "Matron Sylia Lightbringer": Civilian("Sylia Lightbringer", "Cleric", 4, 4, 4, 1.5, 2),
    "Merchant Tavros Goldleaf": Civilian("Tavros Goldleaf", "Merchant", 3, 3, 3, 1.5, 2)
}


misc_npc_names = ["Bedru", "Tucyr", "Ogden", "Gauer", "Fulcor", "Strath", "Hodun-zak", "Gendow", "Sorlon", "Dalvas", "Hap Lu", "Loran", "Arnesan", "Fruela"]

# Town Locations
Town_Locations = {
    "Inn": {
        "Name": "Lazy Dragon Inn and Tavern",
        "Services": ["Rest", "Gossip", "Quests"],
        "Patron": Town_NPCs["Innkeeper Davrid Havenrest"]
    },
    "Blacksmith": {
        "Name": "Bleeding Edge Blacksmith",
        "Services": ["Buy", "Sell", "Upgrade"],
        "Patron": Town_NPCs["Blacksmith Gendry Ironheart"]
    },
    "Alchemist": {
        "Name": "Leaky Cauldron Alchemist",
        "Services": ["Buy", "Sell", "Brew"],
        "Patron": Town_NPCs["Alchemist Elara Moonshadow"]
    },
    "Cleric": {
        "Name": "Temple of Light Cleric",
        "Services": ["Heal", "Bless", "Cure"],
        "Patron": Town_NPCs["Matron Sylia Lightbringer"]
    },
    "General Store": {
        "Name": "General Goods Store",
        "Services": ["Buy", "Sell", "Trade"],
        "Patron": Town_NPCs["Merchant Tavros Goldleaf"]
    }
}
