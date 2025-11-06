"""
projekt1.py: This program is a guess the number game, 
            where the user gets 7 attempts to guess the
            randomly generated number.

__author__ = "Oliver Holmberg"
__version__ = "1.0.0"
__email__ = "oliveraron.holmberg@elev.ga.dbgy.se"
"""

import random
import os
from bcolors import bcolors


running = True

os.system("cls")
print(bcolors.BOLD + bcolors.PURPLE + f"""    ===============================\n===== Welcome to guess the number =====\n    ===============================\n""")
while running:
    tries = 7
    num = random.randint(1, 100)
    print(bcolors.CYAN + f"Guess a number, 1-100, in 7 guesses\n")
    while tries > 0:
        while True:
            guess = input(bcolors.DEFAULT + f"Guess {7-tries+1}/7, (q to exit): ")
            if guess.lower() == "q":
                running = False
                break
            try:
                guess = int(guess)
                break
            except:
                print("You need to guess a number")
                continue
                
        if running == False:
            break
        else:
            if num > guess:
                print(bcolors.RED+ f"The number is larger\n")
                tries -= 1
                continue
            elif num < guess:
                print(bcolors.BLUE+"The number is smaller\n")
                tries -=1
                continue
            else:
                print(bcolors.GREEN + f"\n You got it right in {7-tries+1} guesses")
                break
        
    
    print(bcolors.GREEN + f"\n----- The number was {num} -----")
    if running:
        while True:
            run_again = input(bcolors.DEFAULT + f"\nDo you want to play again?, (y/n): ")
            if run_again.lower() == "y":
                os.system("cls")
                break
            elif run_again.lower() == "n":
                running = False
                break
            else:
                print("Please input (y/n)\n")
    else:
        break
            
    