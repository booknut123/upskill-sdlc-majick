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
from typingStyle import betterTyping, clearConsole, betterInput
import random
import math

class Player:
    classDict = {
        "Rogue": {'maxhp': 35, 'atk': 5, 'defs': 7, 'cooldown': 4},
        "Barbarian": {'maxhp': 40, 'atk': 10, 'defs': 0, 'cooldown': 4},
        "Cleric": {'maxhp': 75, 'atk': 3, 'defs': 5, 'cooldown': 0},
        "Bard": {'maxhp': 50, 'atk': 5, 'defs': 5, 'cooldown': 3},
    }

    def __init__(self, name, lvl, exp, path = 'class1'): # constructor for class Player
        self.name = name
        self.maxhp = self.classDict[path]['maxhp']
        self.currhp = self.classDict[path]['maxhp']
        self.atk = self.classDict[path]['atk']
        self.defs = self.classDict[path]['defs']
        self.lvl = lvl
        self.exp = exp
        self.path = path
        self.cooldown = 0
        self.mock = ['I would say you\'re as ugly as an ogre, but that would be an insult to ogres.', 'No loot is worth having to look at you!', 'There is no beholder\'s eye in which you are beautiful!'] # for bard vicious mockery
    
    # getters & setters
    def getName(self):
        return self.name
    
    def setName(self, nameVal):
        self.name = nameVal

    def getHP(self):
        return self.currhp
    
    def setHP(self, hpVal):
        self.currhp = hpVal
    
    def getMaxHP(self):
        return self.maxhp
    
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
        self.currhp -= amount
    
    def getCooldown(self):
        return self.cooldown
    
    def decCooldown(self):
        self.cooldown -= 1
        
    def boostStat(self):
        statCount = 0
        betterTyping("You can now boost two stats!")
        while statCount < 2: # boosts stats twice
            betterTyping("""Choose a stat to boost:\n +3 HP   +2 ATK  +2 DEF""")
            choice = input("Type HP/ATK/DEF: ").upper().strip()
            if choice in ["HP", "ATK", "DEF"]: 
                statCount += 1
                if choice == "HP":
                    self.maxhp += 3
                    betterTyping(f"Max HP is now {self.maxhp}")
                elif choice == "ATK":
                    self.atk += 2
                    betterTyping(f"ATK is now {self.atk}")
                elif choice == "DEF":
                    self.defs += 2
                    betterTyping(f"DEF is now {self.defs}")
            else:
                betterTyping("Sorry, that isn't a valid stat.")

    def level_up(self): # to reach level x you must complete x/2 more battles
        betterTyping(f"LEVEL UP: {self.lvl} -> {self.lvl+1}")
        self.lvl += 1
        self.maxhp += 10
        self.currhp = self.maxhp
        self.atk += 1
        self.defs += 1
        betterTyping(f"Upgraded stats: HP {self.maxhp} | ATK {self.atk} | DEF {self.defs}")
    