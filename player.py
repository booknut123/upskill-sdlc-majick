'''
Player class:
HP: int
ATK: int
DEFs: int
Level: int
EXP: int

level_up()
attack()

char has base stats, player gets total amount of points to add to each stat

stats
lvl 1: 50 HP, 5 ATK, 5 DEF

'''

class player:
    def __init__(self, hp, atk, defs, lvl, exp): # constructor for class player
        self.hp = hp
        self.atk = atk
        self.defs = defs
        self.lvl = lvl
        self.exp = exp
    
    # getters & setters
    def getHP(self):
        return self.hp
    
    def setHP(self, hpVal):
        self.hp = hpVal
    
    def getATK(self):
        return self.atk
    
    def setATK(self, atkVal):
        self.hp = atkVal

    def getDEFS(self):
        return self.defs
    
    def setDEFS(self, defsVal):
        self.hp = defsVal

    def getLVL(self):
        return self.lvl
    
    def setLVL(self, lvlVal):
        self.hp = lvlVal

    def getEXP(self):
        return self.exp
    
    def setEXP(self, expVal):
        self.hp = expVal
    