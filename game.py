import inspect
from collections import Counter
from hero import Hero

#from dice import roll_hand

#class Game:

#    def start(self):

#        hero = Hero()

#        rolls = roll_hand()

#        print(rolls)
import random as r

hero = Hero()

nums = []
symbols = []
valid_abilities = []
symbol_counts = 0


def has_large_straight(nums):
    return nums == [1,2,3,4,5] or nums == [2,3,4,5,6]

def has_small_straight(nums):
    unique = sorted(set(nums))

    return (
        [1,2,3,4] == unique[:4] or
        [2,3,4,5] == unique[:4] or
        [3,4,5,6] == unique[:4] or
        [1,2,3,4] == unique[-4:] or
        [2,3,4,5] == unique[-4:] or
        [3,4,5,6] == unique[-4:]
    )

def check_abilities():
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

    return valid_abilities, symbol_counts, nums

hero.show_abilities()
attempts = 1

rolls = [r.choice(hero._dice) for _ in range(5)]
for die in rolls:
    print(f"{die['num']} - {die['symbol']}")

while attempts < 3:
    valid_abilities, symbol_counts, nums = check_abilities()

    for i in range(len(rolls)):
        reroll = input(f"Would you like to reroll {rolls[i]}? (y/n) ")

        if reroll.lower() == "y":
            rolls[i] = r.choice(hero._dice)

    for die in rolls:
        print(f"{die['num']} - {die['symbol']}")

    valid_abilities, symbol_counts, nums = check_abilities()

    attempts += 1
    if attempts < 3:
        again = input("Continue rerolling? (y/n) ")

        if again.lower() != "y":
            break



choice = int(input("Choose an ability: "))
selected = valid_abilities[choice - 1]

#self._abilities["smack"]["function"](3)
if selected == "smack":
    hero.smack(symbol_counts["sword"])

elif selected == "fortitude":
    hero.fortitude(symbol_counts["heart"])

else:
    getattr(hero, selected)()