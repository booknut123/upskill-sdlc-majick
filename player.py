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
        return self.currhp
    
    def setHP(self, hpVal):
        self.currhp = hpVal
    
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

    def boostStat(self): # prompts the player to boost their stats twice
        for i in range(1, 3):
            print("""Choose a stat to boost:\n +3 HP   +2 ATK  +2 DEFS""")
            choice = input("Type HP/ATK/DEFS: ").upper()
            if choice == "HP":
                 self.maxhp += 3
                 print(f"Max HP is now {self.maxhp}")
            elif choice == "ATK":
                self.atk += 2
                print(f"ATK is now {self.atk}")
            elif choice == "DEFS":
                self.defs += 2
                print(f"DEFS is now {self.defs}")

    def level_up(self): # to reach level x you must complete x/2 more battles
        print(f"LEVEL UP: {self.lvl} -> {self.lvl+1}")
        self.lvl += 1
        self.maxhp += 10
        self.currhp = self.maxhp
        self.atk += 1
        self.defs += 1
        print(f"Current stats: HP {self.maxhp} | ATK {self.atk} | DEF {self.defs}")
