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
            return (0, False)
        victim.takeDMG(trueDMG)
    
        if victim.getHP() <= 0:
            return (trueDMG, True)
        return (trueDMG, False)

    def use_skill(self):
        if self.player.cooldown > 0:
            betterTyping(f"Your skill is still in cooldown! Please wait {self.player.getCooldown()} more turns.")
            self.player_turn()
            return
        
        if self.player.path == "Rogue": # hide and sneak attack
            self.player.cooldown = self.player.classDict['Rogue']['cooldown']
            _ = betterInput("Using skill Hide. Roll to deal damage first! (enter any character) ")
            damage = self.roll()
            
            dmg, isDead = self.attack(self.player, self.enemy, damage)

            if isDead:
                betterTyping(f"You rolled: {damage}! You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()}'s health is 0. {self.enemy.getName()} is dead. Yay!\n")
                self.whoDied = True
                return
            elif dmg == 0:
                betterTyping(f"You rolled: {damage}! You tried to deal damage to {self.enemy.getName()}, but they evaded. {self.enemy.getName()} still has {self.enemy.getHP()} HP.")
            else:
                betterTyping(f"You rolled: {damage}! You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()} has {self.enemy.getHP()} HP.")
                
            self.player.defs += 3
            betterTyping(f"You're now hidden! Your DEF is now {self.player.defs}. If you successfully evade the next attack, you get sneak attack bonus on your attack!")
            damage = self.roll()
        
            dmg, isDead = self.attack(self.enemy, self.player, damage)

            self.player.defs -= 3
            if isDead:
                betterTyping(f"It's the enemy's turn! {self.enemy.getName()} rolled: {damage} and dealt {dmg} damage to you. You now have 0 HP. You died.\n")
                self.whoDied = False
                return
            elif dmg == 0:
                betterTyping(f"It's the enemy's turn! {self.enemy.getName()} rolled: {damage} and tried to deal damage to you, but you evaded! You still have {self.player.getHP()} HP.")
                _ = betterInput("It's your turn! Since you evaded the last attack, you get Sneak Attack! Please roll. (enter any character) ")
                self.player.decCooldown()
                damage = self.roll()
                
                dmg, isDead = self.attack(self.player, self.enemy, damage + self.player.atk)

                if isDead:
                    betterTyping(f"You rolled: {damage}! You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()}'s health is 0. {self.enemy.getName()} is dead. Yay!\n")
                    self.whoDied = True
                    return
                elif dmg == 0:
                    betterTyping(f"You rolled: {damage}! You tried to deal damage to {self.enemy.getName()}, but they evaded. {self.enemy.getName()} still has {self.enemy.getHP()} HP.")
                    self.enemy_turn()
                else:
                    betterTyping(f"You rolled: {damage}! You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()} has {self.enemy.getHP()} HP.")
                    self.enemy_turn()
            else:
                betterTyping(f"It's the enemy's turn! {self.enemy.getName()} rolled: {damage} and dealt {dmg} damage to you. You have {self.player.getHP()} HP.")
                _ = betterInput("It's your turn! Roll to attack. (enter any character) ")
                self.player.decCooldown()
                damage = self.roll()
                
                dmg, isDead = self.attack(self.player, self.enemy, damage + self.atk)

                if isDead:
                    betterTyping(f"You rolled: {damage}! You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()}'s health is 0. {self.enemy.getName()} is dead. Yay!\n")
                    self.whoDied = True
                    return
                elif dmg == 0:
                    betterTyping(f"You rolled: {damage}! You tried to deal damage to {self.enemy.getName()}, but they evaded. {self.enemy.getName()} still has {self.enemy.getHP()} HP.")
                    self.enemy_turn()
                else:
                    betterTyping(f"You rolled: {damage}! You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()} has {self.enemy.getHP()} HP.")
                    self.enemy_turn()
                
        elif self.player.path == "Barbarian": # attack twice on turn
            self.player.cooldown = self.player.classDict['Barbarian']['cooldown']
            _ = betterInput("Using skill Extra Attack. Time to roll your first attack! (enter any character) ")
            self.player.decCooldown()
            damage = self.roll()
            
            dmg, isDead = self.attack(self.player, self.enemy, damage)

            if isDead:
                betterTyping(f"You rolled: {damage}! You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()}'s health is 0. {self.enemy.getName()} is dead. Yay!\n")
                self.whoDied = True
                return
            elif dmg == 0:
                betterTyping(f"You rolled: {damage}! You tried to deal damage to {self.enemy.getName()}, but they evaded. {self.enemy.getName()} still has {self.enemy.getHP()} HP.")
                _ = betterInput("Time for your second attack! (enter any character) ")
                damage = self.roll()
                
                dmg, isDead = self.attack(self.player, self.enemy, damage)

                if isDead:
                    betterTyping(f"You rolled: {damage}! You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()}'s health is 0. {self.enemy.getName()} is dead. Yay!\n")
                    self.whoDied = True
                    return
                elif dmg == 0:
                    betterTyping(f"You rolled: {damage}! You tried to deal damage to {self.enemy.getName()}, but they evaded. {self.enemy.getName()} still has {self.enemy.getHP()} HP.")
                    self.enemy_turn()
                else:
                    betterTyping(f"You rolled: {damage}! You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()} has {self.enemy.getHP()} HP.")
                    self.enemy_turn()
            else:
                betterTyping(f"You rolled: {damage}! You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()} has {self.enemy.getHP()} HP.")
                _ = betterInput("Time for your second attack! (enter any character) ")
                damage = self.roll()
                
                dmg, isDead = self.attack(self.player, self.enemy, damage)

                if isDead:
                    betterTyping(f"You rolled: {damage}! You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()}'s health is 0. {self.enemy.getName()} is dead. Yay!\n")
                    self.whoDied = True
                    return
                elif dmg == 0:
                    betterTyping(f"You rolled: {damage}! You tried to deal damage to {self.enemy.getName()}, but they evaded. {self.enemy.getName()} still has {self.enemy.getHP()} HP.")
                    self.enemy_turn()
                else:
                    betterTyping(f"You rolled: {damage}! You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()} has {self.enemy.getHP()} HP.")
                    self.enemy_turn()
               
        elif self.player.path == "Cleric": # heal instead of attack on turn
            self.player.cooldown = self.player.classDict['Cleric']['cooldown']
            betterInput("Using skill Healing Word. Roll for points: (enter any character)")
            self.player.decCooldown()
            numPoints = self.roll()
            self.player.currhp += numPoints + self.player.lvl
            if self.player.currhp > self.player.maxhp: self.player.currhp = self.player.maxhp
            betterTyping(f"You rolled: {numPoints}. You healed {numPoints + self.player.lvl} points and are now at {self.player.currhp}HP.")
            self.enemy_turn()
            
        elif self.player.path == "Bard": # deal extra damage before your turn
            thisMock = self.player.mock[random.randint(1, len(self.player.mock) - 1)]
            self.player.cooldown = self.player.classDict['Bard']['cooldown']

            _ = betterInput("You cast Vicious Mockery! Roll for extra damage before your attack:")
            damage = self.roll()
        
            dmg, isDead = self.attack(self.player, self.enemy, math.ceil(damage / 4) + self.player.lvl)

            if isDead:
                betterTyping(f"With a loud '{thisMock}', you dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()}'s health is 0. {self.enemy.getName()} is dead. Yay!\n")
                self.whoDied = True
                return
            elif dmg == 0:
                betterTyping(f"With a loud '{thisMock}', you tried to deal {dmg}damage to {self.enemy.getName()}, but the enemy was unfazed. {self.enemy.getName()} still has {self.enemy.getHP()} HP.")
                numDamage = betterInput("It's time to take your attack! Roll for damage:")
                damage = self.roll()
            
                dmg, isDead = self.attack(self.player, self.enemy, damage)

                if isDead:
                    betterTyping(f"You rolled: {damage}! You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()}'s health is 0. {self.enemy.getName()} is dead. Yay!\n")
                    self.whoDied = True
                    return
                elif dmg == 0:
                    betterTyping(f"You rolled: {damage}! You tried to deal damage to {self.enemy.getName()}, but they evaded. {self.enemy.getName()} still has {self.enemy.getHP()} HP.")
                    self.enemy_turn()
                else:
                    betterTyping(f"You rolled: {damage}! You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()} has {self.enemy.getHP()} HP.")
                    self.enemy_turn()
            else:
                betterTyping(f"With a loud '{thisMock}', you dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()} has {self.enemy.getHP()} HP.")
                numDamage = betterInput("It's time to take your attack! Roll for damage:")
                damage = self.roll()
            
                dmg, isDead = self.attack(self.player, self.enemy, damage)

                if isDead:
                    betterTyping(f"You rolled: {damage}! You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()}'s health is 0. {self.enemy.getName()} is dead. Yay!\n")
                    self.whoDied = True
                    return
                elif dmg == 0:
                    betterTyping(f"You rolled: {damage}! You tried to deal damage to {self.enemy.getName()}, but they evaded. {self.enemy.getName()} still has {self.enemy.getHP()} HP.")
                    self.enemy_turn()
                else:
                    betterTyping(f"You rolled: {damage}! You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()} has {self.enemy.getHP()} HP.")
                    self.enemy_turn()

    def player_turn(self):
        choice = betterInput("It's your turn! Roll to attack or enter 'skill' to use your class skill. (enter any character or 'skill') ")
        if choice.lower() != 'skill':
            self.player.decCooldown()
            damage = self.roll()
            
            dmg, isDead = self.attack(self.player, self.enemy, damage)

            if isDead:
                betterTyping(f"You rolled: {damage}! You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()}'s health is 0. {self.enemy.getName()} is dead. Yay!\n")
                self.whoDied = True
                return
            elif dmg == 0:
                betterTyping(f"You rolled: {damage}! You tried to deal damage to {self.enemy.getName()}, but they evaded. {self.enemy.getName()} still has {self.enemy.getHP()} HP.")
                self.enemy_turn()
            else:
                betterTyping(f"You rolled: {damage}! You dealt {dmg} damage to {self.enemy.getName()}. {self.enemy.getName()} has {self.enemy.getHP()} HP.")
                self.enemy_turn()
        else:
            self.use_skill()
    
    def enemy_turn(self):
        damage = self.roll()
        
        dmg, isDead = self.attack(self.enemy, self.player, damage)

        if isDead:
            betterTyping(f"It's the enemy's turn! {self.enemy.getName()} rolled: {damage} and dealt {dmg} damage to you. You now have 0 HP. You died.\n")
            self.whoDied = False
            return
        elif dmg == 0:
            betterTyping(f"It's the enemy's turn! {self.enemy.getName()} rolled: {damage} and tried to deal damage to you, but you evaded! You still have {self.player.getHP()} HP.")
            self.player_turn()
        else:
            betterTyping(f"It's the enemy's turn! {self.enemy.getName()} rolled: {damage} and dealt {dmg} damage to you. You have {self.player.getHP()} HP.")
            self.player_turn()
        
    def battle(self):
        betterTyping(f"\n{self.enemy.getName()} approaches you. | HP: {self.enemy.getHP()} | ATK: {self.enemy.getATK()} | DEF: {self.enemy.getDEFS()} |")
        _ = betterInput(f"You're starting at {self.player.getHP()} HP. Roll for initiative! (enter any character)")
        
        player_roll = self.roll()
        enemy_roll = self.roll()
        
        betterTyping(f'You rolled: {player_roll}!')
        betterTyping(f'{self.enemy.getName()} rolled: {enemy_roll}!')

        while (player_roll == enemy_roll):
            _ = betterInput("You tied. Roll again! (enter any character)")
            player_roll = self.roll()
            enemy_roll = self.roll()
            betterTyping(f'You rolled: {player_roll}!')
            betterTyping(f'{self.enemy.getName()} rolled: {enemy_roll}!')

        if (player_roll > enemy_roll):
            betterTyping("You rolled higher!")
            self.player_turn()
        else:
            betterTyping(f"{self.enemy.getName()} rolled higher. Watch out!")
            self.enemy_turn()

        if self.whoDied:
            self.num_battles += 1
            self.total_num_battles += 1
            self.numTurnsForEnemy += 1
            self.player.boostStat()
            if self.num_battles == math.ceil(self.player.getLVL() / 2):
                self.player.level_up()
                self.num_battles = 0
            self.reset()
            
        return
    
    def reset(self):
        self.enemy.setHP(45 + (self.numTurnsForEnemy//5) * 10)
        self.enemy.setATK(2 + (self.numTurnsForEnemy//3) * 10)
        self.enemy.setDEFS(3 + (self.numTurnsForEnemy//3) * 10)
        self.enemy.newName()
        self.battle()

    def start(self):
        clearConsole()
        
        betterTyping("Battle starting.")
        self.battle()
        
        betterTyping("Game over.")
        betterTyping(f"Total stats at time of death: {self.player.getMaxHP()} HP, {self.player.getATK()} ATK, {self.player.getDEFS()} DEF\nTotal enemies killed: {self.total_num_battles}")
        if betterInput("Start over? (yes/no)", '\n').lower() == "yes":
            self.__init__(name)
        else:
            betterTyping("Thank you for playing!")
    
    def __init__(self, name):
        self.confirm = True
        
        self.player = player.Player(name, 1, 0, 'Rogue') 
        self.classList = list(self.player.classDict.keys())

        while self.confirm:
            classChoice = betterInput(f'Choose your class from {", ".join(self.classList)}:', '\n').capitalize()
            
            if classChoice not in self.classList:
                betterTyping("Invalid class choice, try again.")
            else:
                betterTyping(f'You chose {classChoice}!')
                self.player = player.Player(name, 1, 0, classChoice)
                betterTyping(f"Your starting stats are: HP: {self.player.getHP()} | ATK: {self.player.getATK()} | DEF: {self.player.getDEFS()}")

                if betterInput("Do you want to choose a different class? (yes/no)").lower() == "no":
                    self.confirm = False
            clearConsole()

        self.enemy = enemy.Enemy ("Slime", 45, 2, 3)
        self.num_battles = 0
        self.total_num_battles = 0
        self.numTurnsForEnemy = 0
        self.start()

clearConsole()
choice = betterInput('Do you want to start the game? (yes/no)')

if choice.lower() == 'yes':
    name = str(betterInput("Enter your character's name:"))
    betterTyping(f"Welcome to Majick, {name}!")
    betterTyping("-------------------")    
    betterTyping("As a new adventurer, you must battle enemies to gain exp and level up your stats (ATK, DEF, and HP). When you reach 0 HP you die, so be careful!")
    betterTyping("Damage is calculated by adding your ATK to a d20, then subtracting the enemy's DEF. Good luck!")
    betterTyping("-------------------")
    game = Game(name)
