from collections import Counter
import random as r
from hero import Hero

class Barbarian(Hero):
    def __init__(self):
        super().__init__("Barbarian", 30)
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
                "description": "Deal 4/6/8 damage",
                "function": self.smack,
                "defendable": True
            },
            "fortitude": {
                "requirement": "3/4/5 hearts",
                "description": "Heal 4/5/6 health",
                "function": self.fortitude,
                "defendable": False
            },
            "sturdyBlow": {
                "requirement": "2 swords + 2 pow",
                "description": "Deal 4 undefendable damage",
                "function": self.sturdyBlow,
                "defendable": False
            },
            "overpower": {
                "requirement": "3 swords + 2 pow",
                "description": "Roll 3 dice and deal their total. Concussion on 14+",
                "function": self.overpower,
                "defendable": True
            },
            "mightyBlow": {
                "requirement": "small straight",
                "description": "deal 9 damage",
                "function": self.mightyBlow,
                "defendable": True
            },
            "reckless": {
                "requirement": "large straight",
                "description": "deal 15 damage. recieve 4 damage back if any damage is successfully dealt",
                "function": self.reckless,
                "defendable": True
            },
            "critBash": {
                "requirement": "4 pow",
                "description": "inflict stun then deal 5 undefendable damage",
                "function": self.critBash,
                "defendable": False
            },
            "rage": {
                "requirement": "5 pow",
                "description": "Ultimate! (dice may be altered to prevent an ultimate. " \
                    "otherwise, no action of any kind may be performed by any opponent until the ability fully completes)." \
                    "inflict stun then deal 15 damage",
                "function": self.rage,
                "defendable": False
            }
        }

    def smack(self, swords):
        dmg = {
        3: 4,
        4: 6,
        5: 8
        }[swords]

        print(f"Smack deals {dmg} damage")
        return {
        "damage": dmg,
        "heal": 0,
        "defendable": True
        }
    
    def fortitude(self, hearts):
        heal = {
        3: 4,
        4: 5,
        5: 6
        }[hearts]

        print(f"fortitude heals {heal} health")
        return {
        "damage": 0,
        "heal": heal,
        "defendable": False
        }

    def sturdyBlow(self):
        dmg = 4
        print(f"sturdy blow deals {dmg} undefendable damage")
        return {
        "damage": 4,
        "heal": 0,
        "defendable": False
        }

    def overpower(self):
        rolls = [r.choice(self._dice) for _ in range(3)]
        for die in rolls:
            print(f"{die['num']} - {die['symbol']}")
        nums = [die["num"] for die in rolls]
        dmg = sum(nums)
        if dmg >= 14:
            inflict = "concussion"
            print(f"overpower deals {dmg} damage and inflicts {inflict}")
        else:
            print(f"overpower deals {dmg} damage")
        return {
        "damage": dmg,
        "heal": 0,
        "defendable": True
        }

    def mightyBlow(self):
        dmg = 9
        print(f"mighty blow deals {dmg} damage")
        return {
        "damage": 9,
        "heal": 0,
        "defendable": True
        }

    def reckless(self):
        dmg = 15
        selfdmg = 4
        print(f"reckless deals {dmg} damage if any damage is dealt sucessfully you take {selfdmg} in return")
        return {
        "damage": 15,
        #"selfDamage": selfdmg,
        "heal": 0,
        "defendable": True
        }

    def critBash(self):
        inflict = "stun"
        dmg = 5
        print(f"crit bash inflicts {inflict} then deals {dmg} undefendable damage")
        return {
        "damage": 5,
        "heal": 0,
        "defendable": False
        }

    def thickSkin(self, description=True):
        rolls = [r.choice(self._dice) for _ in range(3)]
        for die in rolls:
            print(f"{die['num']} - {die['symbol']}")
        symbols = sorted(die["symbol"] for die in rolls)
        symbol_counts = Counter(symbols)
        heal = symbol_counts["heart"] * 2
        
        print(f"Thick Skin heals {heal} health")
        self.health += heal

    def rage(self):
        dmg = 15
        inflict = "stun"
        print(f"rage inflicts {inflict} then deals {dmg} undefendable damage")
        return {
        "damage": 15,
        "heal": 0,
        "defendable": False
        }

    def defense(self):
        self.thickSkin()