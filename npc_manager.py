# For generating and managing NPCs, including enemies and allies.

class Enemy:
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


enemy_creature = Enemy("Goblin", "Humanoid", 1, 50, 50, 2, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 100)
print(f"Enemy Attack: {enemy_creature.combat_power()[0]} Enemy Defense: {enemy_creature.combat_power()[1]}")
print(f"Enemy Magic Attack: {enemy_creature.magic_power()[0]} Enemy Magic Defense: {enemy_creature.magic_power()[1]}")
print(f"Enemy Social Attack: {enemy_creature.social_power()[0]} Enemy Social Defense: {enemy_creature.social_power()[1]}")
