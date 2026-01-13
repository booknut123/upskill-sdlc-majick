'''
Enemy class:
Name: string
HP: int
ATK: int
DEF: int
Level: int

attack()

stats
lvl 1: 45 HP, 2 ATK, 
'''

class enemy:
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