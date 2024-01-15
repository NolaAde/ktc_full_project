# Import dependencies
# A dependency is a libary or module that our code needs to function
import time #to make the code interactive from
from colorama import Fore, Style, init # color text on the terminal

#launch  coloroma
init(autoreset = True)

player_score = 0

def introduction():
    # Welcome the player
    print(Fore.LIGHTMAGENTA_EX+"Welcome to python adventure")
    time.sleep(2)
    player_name = input(Fore.RED+"What's your name?")
    time.sleep(2)
    print(f"hi {player_name}, nice to meet you!")
    time.sleep(2)

show = introduction()