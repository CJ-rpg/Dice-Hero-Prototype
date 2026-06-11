import numpy as np
import random as r
import inspect


class Hero(object):
    def __init__(self):
        self._dice = [
            {"num": 1, "symbol": "sword"},
            {"num": 2, "symbol": "sword"},
            {"num": 3, "symbol": "sword"},
            {"num": 4, "symbol": "heart"},
            {"num": 5, "symbol": "heart"},
            {"num": 6, "symbol": "pow"},
        ]

        self._abilities = {
            "smack": {
                "requirement": "3/4/5 swords",
                "description": "Deal 4/6/8 damage"
                #possibly add later on
                #"function": self.smack
            },
            "fortitude": {
                "requirement": "3/4/5 hearts",
                "description": "Heal 4/5/6 health"
            },
            "SturdyBlow": {
                "requirement": "2 swords + 2 pow",
                "description": "Deal 4 undefendable damage"
            },
            "overpower": {
                "requirement": "3 swords + 2 pow",
                "description": "Roll 3 dice and deal their total. Concussion on 14+"
            },
            "mightyBlow": {
                "requirement": "small straight",
                "description": "deal 9 damage"
            },
            "Reckless": {
                "requirement": "large straight",
                "description": "deal 15 damage. recieve 4 damage back if any damage is successfully dealt"
            },
            "CritBash": {
                "requirement": "4 pow",
                "description": "inflict stun then deal 5 undefendable damage"
            },
            "Rage": {
                "requirement": "5 pow",
                "description": "Ultimate! (dice may be altered to prevent an ultimate. " \
                    "otherwise, no action of any kind may be performed by any opponent until the ability fully completes)." \
                    "inflict stun then deal 15 damage"
            }
        }
    def show_abilities(self):
        for name, info in self._abilities.items():
            print(f"\n{name}")
            print(f"Requirement: {info['requirement']}")
            print(f"Effect: {info['description']}")

    def smack(self, swords):
        dmg = {
        3: 4,
        4: 6,
        5: 8
        }[swords]

        print(f"Smack deals {dmg} damage")
    
    def fortitude(self, hearts):
        heal = {
        3: 4,
        4: 5,
        5: 6
        }[hearts]

        print(f"fortitude heals {heal} health")

    def sturdyBlow(self):
        dmg = 4
        print(f"sturdy blow deals {dmg} undefendable damage")

    def overpower(self):
        dmg = 0
        rolls = [r.choice(self._dice) for _ in range(3)]
        for die in rolls:
            print(f"{die['num']} - {die['symbol']}")
        nums = [die["num"] for die in rolls]
        for num in nums:
            dmg = dmg + num
        if dmg >= 14:
            inflict = "concussion"
            print(f"overpower deals {dmg} damage and inflicts {inflict}")
        else:
            print(f"overpower deals {dmg} damage")

    def mightyBlow(self):
        dmg = 9
        print(f"mighty blow deals {dmg} damage")

    def reckless(self):
        dmg = 15
        selfdmg = 4
        print(f"reckless deals {dmg} damage if any damage is dealt sucessfully you take {selfdmg} in return")

    def critBash(self):
        inflict = "stun"
        dmg = 5
        print(f"crit bash inflicts {inflict} then deals {dmg} undefendable damage")

    #possibly include heart parameter
    def thickSkin(self, description=True):
        if description == True:
            print("Defense roll 3 dice. heal 2 * heart")
        else:
            print("doing attack")
            #heal = 2 * hearts

    def rage(self):
        dmg = 15
        inflict = "stun"
        print(f"rage inflicts {inflict} then deals {dmg} undefendable damage")
