from collections import Counter
from barbarian import Barbarian
from dice import has_large_straight, has_small_straight
import random as r


class Game:

    def __init__(self):
        self.hero = Barbarian()
        self.rolls = []
        self.valid_abilities = []

    def start(self):
        self.hero.show_abilities()
        attempts = 0

        self.rolls = [r.choice(self.hero._dice) for _ in range(5)]
        self.show_rolls()

        while attempts < 2:
            self.valid_abilities, symbol_counts = check_abilities(self.hero, self.rolls)

            for i in range(len(self.rolls)):
                reroll = input(f"Would you like to reroll {self.rolls[i]}? (y/n) ")

                if reroll.lower() == "y":
                    self.rolls[i] = r.choice(self.hero._dice)

            self.show_rolls()

            self.valid_abilities, symbol_counts = check_abilities(self.hero, self.rolls)

            attempts += 1
            if attempts < 2:
                again = input("Continue rerolling? (y/n) ")

                if again.lower() != "y":
                    break



        choice = int(input("Choose an ability: "))
        selected = self.valid_abilities[choice - 1]

        #self._abilities["smack"]["function"](3)
        if selected == "smack":
            self.hero.smack(symbol_counts["sword"])
        elif selected == "fortitude":
            self.hero.fortitude(symbol_counts["heart"])
        else:
            getattr(self.hero, selected)()

    def player_turn(self):
        pass

    def attack_phase(self):
        pass

    def show_rolls(self):
        for die in self.rolls:
            print(f"{die['num']} - {die['symbol']}")

def check_abilities(hero, rolls):
    nums = [die["num"] for die in rolls]   
    symbols = sorted(die["symbol"] for die in rolls)

    symbol_counts = Counter(symbols)
    valid_abilities = []

    if symbol_counts["pow"] >= 5:
        valid_abilities.append("rage")
    if symbol_counts["pow"] >= 4:
        valid_abilities.append("critBash")
    if has_large_straight(nums):
        valid_abilities.append("reckless")
    if has_small_straight(nums):
        valid_abilities.append("mightyBlow")
    if symbol_counts["sword"] >= 3 and symbol_counts["pow"] >= 2:
        valid_abilities.append("overpower")
    if symbol_counts["sword"] >= 2 and symbol_counts["pow"] >= 2:
        valid_abilities.append("sturdyBlow")
    if symbol_counts["sword"] >= 3:
        valid_abilities.append("smack")
    if symbol_counts["heart"] >= 3:
        valid_abilities.append("fortitude")

    print("valid abilities:")
    for i, ability in enumerate(valid_abilities, start=1):
        info = hero._abilities[ability]

        print(
            f"{i}. {ability} "
            f"({info['requirement']}) - "
            f"{info['description']}"
        )

    return valid_abilities, symbol_counts
