import time
import sys
import os

def betterTyping(text, endStyle="\n"):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    print(endStyle, end='')

def betterInput(text, endStyle=" "):
    betterTyping(text, endStyle)
    userInput = input()
    return userInput

def clearConsole():
    os.system('cls') if os.name == 'nt'else os.system('clear')