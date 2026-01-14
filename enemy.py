'''
Enemy class:
Name: string
HP: int
ATK: int
DEF: int

stats
lvl 1: 45 HP, 2 ATK, 3 DEFS
'''

class enemy:
    def __init__(self, name, hp, atk, defs): # constructor for class player
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defs = defs
    
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

    def takeDMG(amount): # the enemy takes damage
        hp -= amount