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

print(bcolors.BOLD + bcolors.PURPLE + bcolors.UNDERLINE + f"----- Welcome to guess the number -----\n")
while running:
    tries = 7
    os.system("cls")
    num = random.randint(1, 100)
    print(bcolors.DEFAULT + f"Guess a number, 1-100, in 7 guesses\n")
    while tries > 0:
        try:
            while True:
                guess = input(bcolors.DEFAULT + f"Guess {7-tries+1}/7, (q to exit): ")
                if guess == "q":
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
                guess = int(guess)
                if num > guess:
                    print(bcolors.RED+ f"\nThe number is larger")
                    tries -= 1
                    continue
                elif num < guess:
                    print(bcolors.RED+"\nThe number is smaller")
                    tries -=1
                    continue
                else:
                    print(bcolors.GREEN + f"\n You got it right in {7-tries+1} guesses")
                    break
        except:
            continue
    
    print(bcolors.GREEN + f"\n----- The number was {num} -----")
    if running:
        while True:
            run_again = input(bcolors.DEFAULT + f"\nDo you want to play again?, (y/n): ")
            if run_again == "y":
                break
            elif run_again == "n":
                running = False
                break
            else:
                print("Please input (y/n)\n")
    else:
        break
            
    