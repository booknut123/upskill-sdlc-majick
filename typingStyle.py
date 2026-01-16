import time
import sys
import os
import io
from contextlib import redirect_stdout

def betterTyping(text, endStyle="\n", sleepTimer = 0.02):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(sleepTimer)
    print(endStyle, end='')

def betterInput(text, endStyle=" "):
    betterTyping(text, endStyle)
    userInput = input()
    if userInput.lower() == "q":
        sys.exit()
    return userInput

def clearConsole():
    os.system('cls') if os.name == 'nt'else os.system('clear')