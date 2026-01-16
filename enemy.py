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
    listOfNames = ['Paper Bird','The Fiery Butcher Freak','The Defiant Weirdo','Webbug','The Creepy Creeper','The Brutal Jester Gorilla','The Dead Thing']
    statDict = {'Paper Bird': {'HP': 45, "DEFS": 3, "ATK": 2}, 
                'The Fiery Butcher Freak': {'HP': 25, "DEFS": 3, "ATK": 6}, 
                'The Defiant Weirdo': {'HP': 35, "DEFS": 7, "ATK": 2}, 
                "Webbug": {'HP': 20, "DEFS": 4, "ATK": 3}, 
                "The Creepy Creeper": {'HP': 10, "DEFS": 3, "ATK": 8}, 
                'The Brutal Jester Gorilla': {'HP': 45, "DEFS": 5, "ATK": 3}, 
                'The Dead Thing': {'HP': 10, "DEFS": 1, "ATK": 1},
                "Slime": {'HP': 20, "DEFS": 2, "ATK": 2}
                    }


    def __init__(self, name): # constructor for class player
        self.name = name
        self.hp = self.statDict[self.name]["HP"]
        self.atk = self.statDict[self.name]["ATK"]
        self.defs = self.statDict[self.name]["DEFS"]
    
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

    def setNewHP(self, howMuchAdd):
        self.setHP(howMuchAdd + self.statDict[self.name]["HP"])

    def setNewATK(self, howMuchAdd):
        self.setATK(howMuchAdd + self.statDict[self.name]["ATK"])
    
    def setNewDEFS(self, howMuchAdd):
        
        self.setDEFS(howMuchAdd + self.statDict[self.name]["DEFS"])
