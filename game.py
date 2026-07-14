from collections import Counter
from barbarian import Barbarian
from dice import has_large_straight, has_small_straight
import random as r


class Game:

    def __init__(self):
        self.hero = Barbarian()
        self.rolls = []
        self.valid_abilities = []
        self.opponent = Barbarian()
        self.active_player = None

    def start(self):
        self.decide_first_player()

        while self.hero.health > 0 and self.opponent.health > 0:
            self.attack_phase()
            self.player_turn()

        if self.hero.health <= 0:
            print("You lose!")
        else:
            print("You win!")

    def player_turn(self):
        if self.active_player == self.hero:
            self.active_player = self.opponent
        else:
            self.active_player = self.hero

    def decide_first_player(self):
        while self.active_player is None:
            hero_roll = r.choice(self.hero._dice)
            opponent_roll = r.choice(self.opponent._dice)

            print(f"You rolled {hero_roll['num']}")
            print(f"Opponent rolled {opponent_roll['num']}")

            if hero_roll["num"] > opponent_roll["num"]:
                self.active_player = self.hero
                print("You go First")
            elif opponent_roll["num"] > hero_roll["num"]:
                self.active_player = self.opponent
                print("Opponent Goes First")
            else:
                print("Tie! Rolling again...")
            
    def get_opponent(self):
        if self.active_player == self.hero:
            return self.opponent
        return self.hero
    
    def show_rolls(self):
            for die in self.rolls:
                print(f"{die['num']} - {die['symbol']}")

    def attack_phase(self):
        print(f"{self.active_player.name}'s Turn")
        print(f"Heros Health: {self.hero.health}")
        print(f"Opponents Health: {self.opponent.health}")

        self.active_player.show_abilities()
        attempts = 0

        self.rolls = [r.choice(self.active_player._dice) for _ in range(5)]
        self.show_rolls()

        while attempts < 2:
            self.valid_abilities, symbol_counts = check_abilities(self.active_player, self.rolls)

            for i in range(len(self.rolls)):
                reroll = input(f"Would you like to reroll {self.rolls[i]}? (y/n) ")

                if reroll.lower() == "y":
                    self.rolls[i] = r.choice(self.active_player._dice)

            self.show_rolls()

            self.valid_abilities, symbol_counts = check_abilities(self.active_player, self.rolls)

            attempts += 1
            if attempts < 2:
                again = input("Continue rerolling? (y/n) ")

                if again.lower() != "y":
                    break


        if self.valid_abilities == []:
            print("Sorry no Valid Abilities")
            return
        choice = int(input("Choose an ability: "))
        selected = self.valid_abilities[choice - 1]

        #self._abilities["smack"]["function"](3)
        if selected == "smack":
            self.active_player.smack(symbol_counts["sword"])
        elif selected == "fortitude":
            self.active_player.fortitude(symbol_counts["heart"])
        else:
            getattr(self.active_player, selected)()

        defender = self.get_opponent()
        defender.take_damage(10)

    

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
