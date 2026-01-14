"""
Docstring for main

methods: attack(attacker, attackee), subtracts dmg val from attackee's HP, checks their HP val
"""

def game():
    print("Welcome to Majick!")
    print("Battle starting.")
    
    battle()

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
        









choice = input('Do you want to start the game? (yes/no)')

if choice.lower() == 'yes':
    game()
else:
    print("You chose not to start the game or misspelled yes.")