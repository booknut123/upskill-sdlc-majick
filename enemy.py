import random


'''
Enemy class:
Name: string
HP: int
ATK: int
DEF: int

stats
lvl 1: 45 HP, 2 ATK, 3 DEFS
'''

class Enemy:
    listOfNames = ['Dummy1','Dummy2','Dummy3','Dummy4','Dummy5','Dummy6','Dummy7']

    def __init__(self, name, hp, atk, defs): # constructor for class player
        self.name = name
        self.hp = hp
        self.atk = atk
        self.defs = defs
    
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

    def takeDMG(self, amount): # the enemy takes damage
        self.hp -= amount
    
    def newName(self):
        self.setName(self.listOfNames[random.randint(0, len(self.listOfNames)-1)])
