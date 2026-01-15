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
    classDict = {
        "Rogue": {'maxhp': 35, 'atk': 5, 'defs': 7},
        "Barbarian": {'maxhp': 40, 'atk': 10, 'defs': 0},
        "Cleric": {'maxhp': 75, 'atk': 3, 'defs': 5},
        "Bard": {'maxhp': 50, 'atk': 5, 'defs': 5},
    }

    def __init__(self, name, lvl, exp, path = 'class1'): # constructor for class Player
        self.name = name
        self.maxhp = self.classDict[path]['maxhp']
        self.currhp = self.classDict[path]['maxhp']
        self.atk = self.classDict[path]['atk']
        self.defs = self.classDict[path]['defs']
        self.lvl = lvl
        self.exp = exp
        
    
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

    def boostStat(self):
        statCount = 0
        print("You can now boost two stats!")
        while statCount < 2: # boosts stats twice
            print("""Choose a stat to boost:\n +3 HP   +2 ATK  +2 DEF""")
            choice = input("Type HP/ATK/DEF: ").upper()
            if choice in ["HP", "ATK", "DEF"]: 
                statCount += 1
                if choice == "HP":
                    self.maxhp += 3
                    print(f"Max HP is now {self.maxhp}")
                elif choice == "ATK":
                    self.atk += 2
                    print(f"ATK is now {self.atk}")
                elif choice == "DEF":
                    self.defs += 2
                    print(f"DEF is now {self.defs}")
            else:
                print("Sorry, that isn't a valid stat.")

    def level_up(self): # to reach level x you must complete x/2 more battles
        print(f"LEVEL UP: {self.lvl} -> {self.lvl+1}")
        self.lvl += 1
        self.maxhp += 10
        self.currhp = self.maxhp
        self.atk += 1
        self.defs += 1
        print(f"Upgraded stats: HP {self.maxhp} | ATK {self.atk} | DEF {self.defs}")
