# majick 1.0

## Description

“majick” is a simple text-based turn-based combat game based on DND. The goal of the game is to fight as many enemies as you can to get the highest score; if you die, you fail.

You play as a character with three basic stats: health points (HP), attack (ATK), and defense (DEF). The mechanic of the game is fighting enemies in turn-based combat, where you and the enemy take turns hitting each other. The damage both you and the enemy deal is based on a randomized die roll; the total amount of damage dealt is simply ATK + die roll outcome - DEF. Combat can either end in a **failure**, where the enemy kills you (you fall below 0 HP) and the game is over, or **success**, where you kill the enemy and gain points based on its HP. 

## Key Features
This game features
* DND-style turn-based combat
* A D20 to initiate combat and calculate damage dealt
* A points-based level system

## Getting Started

### Dependencies
* Python v3

### Installing
To play majick, you need the following files from the repository:
* `main.py`
* `player.py`
* `enemy.py`
* `typingStyle.py`
Download them onto your device, and run `main.py` to get started. See below for more details. 

### Executing program
You may play this game through any integrated development environment (IDE) by running `main.py` in it. You may also run it in your device's command line interface (CLI), if you have `Python v3` installed and set up.

## Authors
Kailyn Lau, Jessalyn Liang, Mehreen Sajid, Amorie Zsako

## Version History
v1.0

## License

This project is licensed under the MIT License - see the LICENSE.md file for details

## Acknowledgments
Supervisor(s): Michelle Ferreirae, Wellesley College Upskill '26 (SDLC)
Testers: TBD