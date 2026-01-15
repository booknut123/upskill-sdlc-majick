import player
import enemy
import random

"""
Docstring for main

methods: attack(attacker, victim), subtracts dmg val from attackee's HP, checks their HP val
roll(), returns a random number between 1-20
"""

class Game:
    whoDied = True
    def roll(self):
        return random.randint(1, 20)
        
    def attack(self, attacker, victim, rollResult):
        victimDEFS = victim.getDEFS()
        attackerATK = attacker.getATK()
        trueDMG = attackerATK + rollResult - victimDEFS
        
        if trueDMG <= 0:
            print(f"{victim.getName()} you evaded!")
            return (0, False)
        victim.takeDMG(trueDMG)
    
        if victim.getHP() <= 0:
            return (trueDMG, True)
        return (trueDMG, False)

    def player_turn(self):
        _ = input("It's your turn! Roll to attack. (enter any character) ")
        damage = self.roll()
        print(f'You rolled a {damage}!')
        
        dmg, isDead = self.attack(self.player, self.enemy, damage)

        if isDead:
            print(f"You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()}'s health is 0. {self.enemy.getName()} is dead. Yay!")
            self.whoDied = True
            return
        else:
            print(f"You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()} has {self.enemy.getHP()} HP. Enemy's turn.")
            self.enemy_turn()
    
    def enemy_turn(self):
        print("It's the enemy's turn!")
        damage = self.roll()
        print(f'The enemy rolled a {damage}!')
        
        dmg, isDead = self.attack(self.enemy, self.player, damage)

        if isDead:
            print(f"{self.enemy.getName()} dealt {dmg} damage to You. You now have 0 HP. You died.")
            self.whoDied = False
            return
        else:
            print(f"{self.enemy.getName()} dealt {dmg} damage to You. You have {self.player.getHP()} HP.")
            self.player_turn()
        
    def battle(self):
        print("An enemy approaches you. ")
        _ = input("Roll for initiative! (enter any character) ")
        
        player_roll = self.roll()
        enemy_roll = self.roll()
        
        print(f'You rolled a {player_roll}!')
        print(f'The enemy rolled a {enemy_roll}!')

        while (player_roll == enemy_roll):
            _ = input("You tied. Roll again! (enter any character) ")
            player_roll = self.roll()
            enemy_roll = self.roll()
            print(f'You rolled a {player_roll}!')
            print(f'The enemy rolled a {enemy_roll}!')

        if (player_roll > enemy_roll):
            print("You rolled higher!")
            self.player_turn()
        else:
            print("The enemy rolled higher. Watch out!")
            self.enemy_turn()


        if self.whoDied:
            self.reset()

        
        return
    
    def reset(self):
        self.enemy.setHP(45)
        self.enemy.setATK(2)
        self.enemy.setDEFS(3)
        self.enemy.newName()
        self.battle()

    def newGame(self):
        print('adada')
        self.player.setHP(50)
        self.player.setATK(5)
        self.player.setDEFS(5)
        self.player.setLVL(1)
        self.player.setEXP(0)
        self.start()

    def start(self):
        print( "\n" *100)
        print("Welcome to Majick!")
        print("-------------------")    
        print("As a new adventuer, you must battle enemies to gain exp and level up your stats which include ATK, DEF, and HP. When you reach 0 HP you die, so be careful! Damage is calculated by adding your ATK to a random roll between 1-20, then subtracting the enemy's DEF. Good luck!")
        print("Battle starting.")
        
        self.battle()
        
        print("Battle ends.")
    
    def __init__(self, name):
        self.player = player.Player(name, 50, 5, 5, 1, 0) 
        self.enemy = enemy.Enemy("Dummy", 45, 2, 3) # dummy enemy for milestone 1
        self.start()
        
        
        while input("wanna restart?(y/n)").lower() == "y":
            self.newGame()



choice = input('Do you want to start the game? (yes/no)')

if choice.lower() == 'yes':
    name = str(input("Enter your character's name: "))
    game = Game(name)
