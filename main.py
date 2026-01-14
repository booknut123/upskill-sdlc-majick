import player as Player
import enemy as Enemy

"""
Docstring for main

methods: attack(attacker, attackee), subtracts dmg val from attackee's HP, checks their HP val
"""

class Game:
    def _init_(self, name):
        self.name = name
        self.character = Player(50, 5, 5, 1, 0)
        self.enemy = Enemy (45, 2, 3)
        
    def attack(attacker, victim):
        victimDEFS = victim.getDEFS()
        attackerATK = attacker.getATK()
        trueDMG = attackerATK - victimDEFS
        victim.takeDMG(trueDMG)

        if victim.getHP() <= 0:
            print("The Enemy has been defeated!")
            return True
        return False

    def player_turn():
        _ = ("It's your turn! Roll to attack. (enter any character) ")
        damage = roll()
        if attack(self.character, self.enemy):
            return True
    
    def enemy_turn():
        _ = ("It's the enemy's turn!")
        damage = roll()
        if attack(self.character, self.enemy):
            return True
        
    def battle():
        print("An enemy approaches you. ")
        _ = input("Roll for initiative! (enter any character) ")
        player_roll = roll()
        enemy_roll = roll()
        while(player_roll == enemy_roll):
            _ = input("You tied. Roll again! (enter any character) ")
            player_roll = roll()
            enemy_roll = roll()
        if (player_roll > enemy_roll):
            print("You rolled higher!")
            player_turn()
        else:
            print("The enemy rolled higher. Watch out!")
            enemy_turn()

    
    
    def start():
        print("Welcome to Majick!")
        print("Battle starting.")
        
        battle()
    
choice = input('Do you want to start the game? (yes/no)')

if choice.lower() == 'yes':
    name = str(input("Enter your character's name: "))
    Game(name)
    print("Enemy started a fight with you!")
    Game.start()