import player
import enemy

"""
Docstring for main

methods: attack(attacker, attackee), subtracts dmg val from attackee's HP, checks their HP val
"""


class Game:
    def _init_(self, name):
        self.name = name
        self.character = Player(50, 5, 5, 1, 0)

    def attack(attacker, victim):
        victimDEFS = victim.getDEFS()
        attackerATK = attacker.getATK()
        trueDMG = attackerATK - victimDEFS
        victim.takeDMG(trueDMG)

        if victim.getHP() <= 0:
            print("The Enemy has been defeated!")
    
        



choice = input('Do you want to start the game? (yes/no)')

if choice.lower() == 'yes':
    name = str(input("Enter your character's name: "))
    Game(name)
    print("Enemy started a fight with you!")
    Game.start()

else:
    print("You chose not to start the game or misspelled yes.")