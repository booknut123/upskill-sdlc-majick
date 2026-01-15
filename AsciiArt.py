from typingStyle import betterTyping, clearConsole, betterInput
from pynput import keyboard

yesAndNoButNo = " _________________ \n" \
"|                 |\n" \
"|   Yes     <No>  |\n" \
"|_________________|\n" \

yesAndNoButYes = " _________________ \n" \
"|                 |\n" \
"|   <Yes>   No    |\n" \
"|_________________|\n" \

Rouge = " ___________________  \n"\
        "|                   | \n" \
        "| <Rogue>    Bard   |\n" \
        "| Barbarian  Cleric |\n" \
        "|___________________|\n" 

Bard = " ___________________ \n"\
        "|                   | \n" \
        "|  Rogue    <Bard>  |\n" \
        "| Barbarian  Cleric |\n" \
        "|___________________|\n" 
Barbarian = " ___________________  \n"\
            "|                   | \n" \
            "|  Rogue     Bard   |\n" \
            "|<Barbarian> Cleric |\n" \
            "|___________________|\n" 

Cleric =" ___________________  \n"\
        "|                   | \n" \
        "|  Rogue     Bard   |\n" \
        "| Barbarian <Cleric>|\n" \
        "|___________________|\n" 

# flag = True
# def onPress(key):
#     global flag
#     clearConsole()
#     if key == keyboard.Key.esc:
#         return False
#     elif key == keyboard.Key.left:
#         flag = True
#         print(yesAndNoButYes)
#     elif key == keyboard.Key.right:
#         flag = False
#         print(yesAndNoButNo)
#     elif key == keyboard.Key.enter:
#         betterTyping("Yes" if flag else "No", '\n')
#         return False

# def onRelease(key):
#     return


# with keyboard.Listener(on_press=onPress, on_release=onRelease) as keyListener:
#     clearConsole()
#     betterTyping(yesAndNoButYes)
#     keyListener.join()
    




class Options:
    flag = 0
    dictOfArt = {"yesNo": {'No': yesAndNoButNo, "Yes": yesAndNoButYes}, "Classes": {"Bard": Bard, "Barbarian" : Barbarian, "Cleric": Cleric, "Rogue" : Rouge}}

    def onPress(self, key):
        clearConsole()
        if key == keyboard.Key.esc:
            return False
        elif key == keyboard.Key.left:
            if self.flag > 0:
                self.flag -= 1
            print(self.dictOfArt[self.type][self.options[self.flag]])
        elif key == keyboard.Key.right:
            if self.flag < len(self.options)-1:
                self.flag += 1
            print(self.dictOfArt[self.type][self.options[self.flag]])
        elif key == keyboard.Key.enter:
            betterTyping(self.options[self.flag])
            return False
    def onRelease(self, key):
        return
    

    def __init__(self, type, options): 
        self.type = type
        self.options = options

        self.keyListener = keyboard.Listener(on_press=self.onPress, on_release=self.onRelease)
        self.keyListener.daemon = True

        clearConsole()
        betterTyping(self.dictOfArt[self.type][self.options[0]])
        self.keyListener.start()
        self.keyListener.join()


# Options('yesNo', ['Yes', 'No'])
Options('Classes', ['Rogue', 'Bard', "Barbarian", "Cleric"])


