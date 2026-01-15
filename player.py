'''
Player class:
HP: int
ATK: int
DEFs: int
Level: int
EXP: int

base stats
lvl 1: 50 HP, 5 ATK, 5 DEF

stretches:
char has base stats, player gets total amount of points to add to each stat?
level_up()
'''

class Player:
    def __init__(self, name, hp, atk, defs, lvl, exp): # constructor for class Player
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defs = defs
        self.lvl = lvl
        self.exp = exp
    
    # getters & setters
    def getName(self):
        return self.name
    
    def setName(self, nameVal):
        self.name = nameVal

    def getHP(self):
        return self.hp
    
    def setHP(self, hpVal):
        self.hp = hpVal
    
    def getATK(self):
        return self.atk
    
    def setATK(self, atkVal):
        self.atk = atkVal

    def getDEFS(self):
        return self.defs
    
    def setDEFS(self, defsVal):
        self.defs = defsVal

    def getLVL(self):
        return self.lvl
    
    def setLVL(self, lvlVal):
        self.lvl = lvlVal

    def getEXP(self):
        return self.exp
    
    def setEXP(self, expVal):
        self.exp = expVal

    def takeDMG(self, amount): # the player takes damage
        self.hp -= amount
    
    def boostStat():
        for i in range(1, 3): # boosts stats twice
            print("""Choose a stat to boost:
                +3 HP   +2 ATK  +2 DEFS""")
            choice = input("Type HP/ATK/DEFS: ").upper()
            # if choice == "HP": 