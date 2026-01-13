"""
Docstring for main

methods: attack(attacker, attackee), subtracts dmg val from attackee's HP, checks their HP val
"""

choice = input('Do you want to start the game? (yes/no)')

if choice.lower() == 'yes':
    print("Enemy started a fight with you!")
else:
    print("You chose not to start the game or misspelled yes.")