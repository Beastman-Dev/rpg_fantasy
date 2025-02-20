# For generating and managing NPCs, including enemies and allies.

import os

class Combatant:
    def __init__(self, name, type, challenge_rating, max_hp, max_mana, physical, mental, social, combat_skill, magic_skill, charm_skill, weapon_modifier, spell_modifier, social_modifier, physical_resistance, magic_resistance, charm_resistance, exp):
        self.name = name
        self.type = type
        self.challenge_rating = challenge_rating
        self.current_hp = max_hp
        self.max_hp = max_hp
        self.current_mana = max_mana
        self.max_mana = max_mana
        self.physical = physical
        self.mental = mental
        self.social = social
        self.combat_skill = combat_skill
        self.magic_skill = magic_skill
        self.charm_skill = charm_skill
        self.weapon_modifier = weapon_modifier
        self.spell_modifier = spell_modifier
        self.social_modifier = social_modifier
        self.physical_resistance = physical_resistance
        self.magic_resistance = magic_resistance
        self.charm_resistance = charm_resistance
        self.exp = exp

    def combat_power(self):
        attack = self.physical + self.combat_skill * self.weapon_modifier
        defense = self.combat_skill + self.physical_resistance
        return attack, defense

    def magic_power(self):
        magic_attack = self.mental + self.magic_skill * self.spell_modifier
        magic_defense = self.magic_skill + self.magic_resistance
        return magic_attack, magic_defense
    
    def social_power(self):
        social_attack = self.social + self.charm_skill * self.social_modifier
        social_defense = self.social + self.charm_resistance
        return social_attack, social_defense

class Civilian:
    def __init__(self, name, type, mental, social, charm_skill, social_modifier, charm_resistance):
        self.name = name
        self.type = type
        self.mental = mental
        self.social = social
        self.charm_skill = charm_skill
        self.social_modifier = social_modifier
        self.charm_resistance = charm_resistance

    def social_power(self):
        social_attack = self.social + self.charm_skill * self.social_modifier
        social_defense = self.social + self.charm_resistance
        return social_attack, social_defense
    
class NPCManager:
    def __init__(self):
        self.npcs = []
        self.civilians = []
        self.enemies = []
        self.allies = []

    def add_npc(self, npc):
        self.npcs.append(npc)
        if npc.type == "Enemy":
            self.enemies.append(npc)
        elif npc.type == "Ally":
            self.allies.append(npc)
        elif npc.type == "Civilian":
            self.civilians.append(npc)

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")
    return

def test_npcs():
    npc_manager = NPCManager()
    goblin = Combatant("Goblin", "Enemy", 1, 50, 50, 2, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 100)
    npc_manager.add_npc(goblin)
    hired_sword = Combatant("Hired Sword", "Ally", 1, 50, 50, 2, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 100)
    npc_manager.add_npc(hired_sword)
    blacksmith = Civilian("Blacksmith", "Civilian", 1, 1, 1, 1, 1)
    npc_manager.add_npc(blacksmith)

def unit_test():
    npc_manager = NPCManager()
    goblin = Combatant("Goblin", "Enemy", 1, 50, 50, 2, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 100)
    npc_manager.add_npc(goblin)
    clear_screen()
    print("NPC Manager Test")
    print(f"\n  NPC: {npc_manager.enemies[0].name}")
    print(f"  Attack/Defense: {npc_manager.enemies[0].combat_power()}")
    print(f"  Magic A/D: {npc_manager.enemies[0].magic_power()}")
    print(f"  Social A/D: {npc_manager.enemies[0].social_power()}")
    blacksmith = Civilian("Blacksmith", "Civilian", 1, 1, 1, 1, 1)
    npc_manager.add_npc(blacksmith)
    print(f"\n  NPC: {npc_manager.civilians[0].name}")
    print(f"  Social A/D: {npc_manager.civilians[0].social_power()}")
    hired_sword = Combatant("Hired Sword", "Ally", 1, 50, 50, 2, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 100)
    npc_manager.add_npc(hired_sword)
    print(f"\n  NPC: {npc_manager.allies[0].name}")
    print(f"  Combat Attack/Defense: {npc_manager.allies[0].combat_power()}")
    print(f"  Magic A/D: {npc_manager.allies[0].magic_power()}")
    print(f"  Social A/D: {npc_manager.allies[0].social_power()}")

#unit_test()