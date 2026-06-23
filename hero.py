
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health
        self._dice = []
        self._abilities = []
        self.combat_points = 0

    def take_damage(self, amount):
        self.health -= amount

    def heal(self, amount):
        self.health += amount

    def gain_cp(self, amount):
        self.combat_points += amount

    def show_abilities(self):
        for name, info in self._abilities.items():
            print(f"\n{name}")
            print(f"Requirement: {info['requirement']}")
            print(f"Effect: {info['description']}")
