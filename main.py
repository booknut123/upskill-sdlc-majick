import player as Player
import enemy as Enemy
import random

"""
Docstring for main

methods: attack(attacker, attackee), subtracts dmg val from attackee's HP, checks their HP val
roll(), returns a random number between 1-20
"""

class Game:
    def _init_(self, name):
        self.name = name
        self.character = Player(50, 5, 5, 1, 0)
        self.enemy = Enemy (45, 2, 3)
    
    def roll():
        return random.randint(1,20)
        
    def attack(attacker, victim, rollResult):
        victimDEFS = victim.getDEFS()
        attackerATK = attacker.getATK()
        trueDMG = attackerATK + rollResult - victimDEFS
        victim.takeDMG(trueDMG)

        if victim.getHP() <= 0:
            print(f"{victim.getNAME()} has been defeated!")
            return True
        return False

    def player_turn(self):
        _ = ("It's your turn! Roll to attack. (enter any character) ")
        damage = self.roll()
        if self.attack(self.character, self.enemy, damage):
            return True
        else:
            self.enemy_turn()
    
    def enemy_turn(self):
        _ = ("It's the enemy's turn!")
        damage = self.roll()
        if self.attack(self.character, self.enemy, damage):
            return True
        else:
            self.enemy_turn()
        
    def battle(self):
        print("An enemy approaches you. ")
        _ = input("Roll for initiative! (enter any character) ")
        player_roll = self.roll()
        enemy_roll = self.roll()
        while(player_roll == enemy_roll):
            _ = input("You tied. Roll again! (enter any character) ")
            player_roll = self.roll()
            enemy_roll = self.roll()
        if (player_roll > enemy_roll):
            print("You rolled higher!")
            self.player_turn()
        else:
            print("The enemy rolled higher. Watch out!")
            self.enemy_turn()
    
    def start(self):
        print("Welcome to Majick!")
        print("Battle starting.")
        
        self.battle()
    
choice = input('Do you want to start the game? (yes/no)')

if choice.lower() == 'yes':
    name = str(input("Enter your character's name: "))
    Game(name)
    print("Enemy started a fight with you!")
