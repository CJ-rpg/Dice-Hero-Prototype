import numpy as np

class Hero(object):
    def init(self):
        self._dice = [
            {"num": 1, "symbol": "sword"},
            {"num": 2, "symbol": "sword"},
            {"num": 3, "symbol": "sword"},
            {"num": 4, "symbol": "heart"},
            {"num": 5, "symbol": "heart"},
            {"num": 6, "symbol": "pow"},
        ]
    
    def traverse(self, function=print):
        for j in range(len(self._dice)):
            function(self._dice[j])

    def smack(self):
        print("3 sword or 4 sword or 5 sword")
        print("deal 4 dmg for 3 swords, 6 dmg for 4 swords, 8, dmg for 5 swords")
        #dmg = 4 or 6 or 10
    
    def fortitude(self):
        print("3 heart or 4 heart or 5 heart")
        print(" heal 4 for 3 hearts, 5 for 4 hearts, 6 for 5 hearts")
        #heal = 4 or 5 or 6

    def sturdyBlow(self):
        print("2 sword 2 pow")
        print("deal 4 undefendablee dmg")
        #dmg = 4

    def overpower(self):
        print("3 swords 2 pow")
        print("roll 3 dice: the deal dmg equal to the total roll value. if the roll value is at least 14, inflict concussion.")
        #dmg = 15
        #inflict = concussion

    def mightyBlow(self):
        print("small straight")
        print("deal 9 dmg")
        #dmg = 9

    def reckless(self):
        print ("large straight")
        print("deal 15 dmg, recieve 4 dmg in return. (return dmg only applies if at least 1 dmg was dealt successfully)")
        #dmg = 15
        #selfdmg = 4

    def critBash(self):
        print("4 pow")
        print("inflict Stun Then deal 5 undefendable dmg")
        #inflict = stun
        # #dmg = 5

    def thickSkin(self):
        print("Defense roll 3 dice. heal 2 * heart")
        #heal = 2 * hearts

    def rage(self):
        print("Ultimate! (dice may be altered to prevent an ultimate. " \
        "otherwise, no action of any kind may be performed by any opponent until the ability fully completes). 5 pow")
        print("inflict Stun deal 15 dmg")
        #inflict = stun
        #dmg = 5
