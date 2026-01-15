import player
import enemy
import random
import math

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
            whoDied = True
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
            whoDied = False
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
            self.num_battles += 1
            print(f"Battles:{self.num_battles}")
            print(f"Level: {self.player.getLVL()}")
            if self.num_battles == math.ceil(self.player.getLVL() / 2):
                self.player.level_up()
                self.num_battles = 0
            self.reset()
            
        return
    
    def reset(self):
        self.enemy.setHP(45)
        self.enemy.setATK(2)
        self.enemy.setDEFS(3)
        self.enemy.newName()
        print(self.enemy.getHP())
        self.battle()


    def start(self):
        print( "\n" *100)
        print("Welcome to Majick!")
        print("Battle starting.")
        
        self.battle()
        
        print("Battle ends.")
    
    def __init__(self, name):
        self.player = player.Player(name, 50, 5, 5, 1, 0) 
        self.enemy = enemy.Enemy ("Dummy", 45, 2, 3) # dummy enemy for milestone 1
        self.num_battles = 0
        self.start()

choice = input('Do you want to start the game? (yes/no) ')

if choice.lower() == 'yes':
    name = str(input("Enter your character's name: "))
    game = Game(name)
