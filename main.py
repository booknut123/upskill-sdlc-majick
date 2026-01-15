import player
import enemy
import random
import math
from typingStyle import betterTyping, clearConsole, betterInput
"""
Docstring for main

methods: attack(attacker, victim), subtracts dmg val from attackee's HP, checks their HP val
roll(), returns a random number between 1-20
"""

class Game:
    whoDied = True # true = enemy dead
    
    def roll(self):
        return random.randint(1, 20)
        
    def attack(self, attacker, victim, rollResult):
        victimDEFS = victim.getDEFS()
        attackerATK = attacker.getATK()
        trueDMG = attackerATK + rollResult - victimDEFS
        
        if trueDMG <= 0:
            betterTyping(f"{victim.getName()} evaded!")
            return (0, False)
        victim.takeDMG(trueDMG)
    
        if victim.getHP() <= 0:
            return (trueDMG, True)
        return (trueDMG, False)

    def player_turn(self):
        _ = betterInput("It's your turn! Roll to attack. (enter any character)")
        damage = self.roll()
        betterTyping(f'You rolled a {damage}!')
        
        dmg, isDead = self.attack(self.player, self.enemy, damage)

        if isDead:
            betterTyping(f"You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()}'s health is 0. {self.enemy.getName()} is dead. Yay!")
            self.whoDied = True
            return
        else:
            betterTyping(f"You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()} has {self.enemy.getHP()} HP. Enemy's turn.")
            self.enemy_turn()
    
    def enemy_turn(self):
        betterTyping("It's the enemy's turn!")
        damage = self.roll()
        betterTyping(f'The enemy rolled a {damage}!')
        
        dmg, isDead = self.attack(self.enemy, self.player, damage)

        if isDead:
            betterTyping(f"{self.enemy.getName()} dealt {dmg} damage to You. You now have 0 HP. You died.")
            self.whoDied = False
            return
        else:
            betterTyping(f"{self.enemy.getName()} dealt {dmg} damage to You. You have {self.player.getHP()} HP.")
            self.player_turn()
        
    def battle(self):
        betterTyping("An enemy approaches you. ")
        _ = betterInput("Roll for initiative! (enter any character)")
        
        player_roll = self.roll()
        enemy_roll = self.roll()
        
        betterTyping(f'You rolled a {player_roll}!')
        betterTyping(f'The enemy rolled a {enemy_roll}!')

        while (player_roll == enemy_roll):
            _ = betterInput("You tied. Roll again! (enter any character)")
            player_roll = self.roll()
            enemy_roll = self.roll()
            betterTyping(f'You rolled a {player_roll}!')
            betterTyping(f'The enemy rolled a {enemy_roll}!')

        if (player_roll > enemy_roll):
            betterTyping("You rolled higher!")
            self.player_turn()
        else:
            betterTyping("The enemy rolled higher. Watch out!")
            self.enemy_turn()

        if self.whoDied:
            self.num_battles += 1
            self.numTurnsForEnemy += 1
            if self.num_battles == math.ceil(self.player.getLVL() / 2):
                self.player.level_up()
                self.num_battles = 0
            self.reset()

        
            
        return
    
    def reset(self):
        self.enemy.setHP(45 + (self.numTurnsForEnemy//5) * 2)
        self.enemy.setATK(2 + (self.numTurnsForEnemy//3) * 2)
        self.enemy.setDEFS(3 + (self.numTurnsForEnemy//3) * 2)
        self.enemy.newName()
        betterTyping(f"Next enemy: {self.enemy.getName()} | HP: {self.enemy.getHP()} | ATK: {self.enemy.getATK()} | DEF: {self.enemy.getDEFS()}")
        self.battle()

    def start(self):
        clearConsole()
        
        betterTyping("Battle starting.")
        self.battle()
        
        betterTyping("Battle ends.")
    
    def __init__(self, name):
        self.confrim = True
        
        self.player = player.Player(name, 1, 0, 'class1') 
        self.classList = list(self.player.classDict.keys())

        while self.confrim:
            classChoice = betterInput(f'Choose your class from {", ".join(self.classList)}', '\n')
            
            if classChoice not in self.classList:
                betterTyping("Invalid class choice, try again.")
            else:
                betterTyping(f'You chose {classChoice}!')
                self.player = player.Player(name, 1, 0, classChoice)
                betterTyping(f"Your starting stats are: HP: {self.player.getHP()} | ATK: {self.player.getATK()} | DEF: {self.player.getDEFS()}")

                if betterInput("Do you want to choose a different class?(y/n)").lower() == "n":
                    self.confrim = False
            clearConsole()

        self.enemy = enemy.Enemy ("Dummy", 45, 2, 3) # dummy enemy for milestone 1
        self.num_battles = 0
        self.numTurnsForEnemy = 0
        self.start()
        
        
        if betterInput("wanna restart? (yes/no)", '\n').lower() == "y":
            self.__init__(name)

clearConsole()
choice = betterInput('Do you want to start the game? (yes/no)')

if choice.lower() == 'yes':
    name = str(betterInput("Enter your character's name:"))
    betterTyping("Welcome to Majick!")
    betterTyping("-------------------")    
    betterTyping("As a new adventuer, you must battle enemies to gain exp and level up your stats which include ATK, DEF, and HP. When you reach 0 HP you die, so be careful! Damage is calculated by adding your ATK to a random roll between 1-20, then subtracting the enemy's DEF. Good luck!")
    game = Game(name)
