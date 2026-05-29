from hero import Hero
#from dice import roll_hand

#class Game:

#    def start(self):

#        hero = Hero()

#        rolls = roll_hand()

#        print(rolls)
import random as r

hero = Hero()

hero.init()

attempts = 1

rolls = [r.choice(hero._dice) for _ in range(5)]
for die in rolls:
    print(f"{die['num']} - {die['symbol']}")

while attempts < 3:
    for i in range(len(rolls)):
        reroll = input(f"Would you like to reroll {rolls[i]}? (y/n) ")

        if reroll.lower() == "y":
            rolls[i] = r.choice(hero._dice)

    for die in rolls:
        print(f"{die['num']} - {die['symbol']}")

    attempts += 1
    if attempts < 3:
        again = input("Continue rerolling? (y/n) ")

        if again.lower() != "y":
            break
nums = sorted(die["num"] for die in rolls)

if nums == [1,2,3,4,5] | nums == [2,3,4,5,6]:
    Hero.reckless()
