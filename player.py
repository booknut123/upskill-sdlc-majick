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
    def __init__(self, name, maxhp, atk, defs, lvl, exp): # constructor for class Player
        self.name = name
        self.maxhp = maxhp
        self.currhp = maxhp
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

    def takeDMG(self, amount): # the player takes damage
        self.currhp -= amount
    
    def level_up(self): # to reach level x you must complete x/2 more battles
        print(f"LEVEL UP: {self.lvl} -> {self.lvl+1}")
        self.lvl += 1
        self.maxhp += 10
        self.currhp = self.maxhp
        self.atk += 1
        self.defs += 1