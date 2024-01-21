# Import dependencies
# A dependency is a libary or module that our code needs to function
import time #to make the code interactive from
from colorama import Fore, Style, init # color text on the terminal

#launch coloroma
init(autoreset = True)

player_score = 0

def introduction():
    # Welcome the player
    print(Fore.LIGHTCYAN_EX+"Welcome to python adventure")
    time.sleep(1)
    player_name = input(Fore.LIGHTBLUE_EX+"What's your name?")
    time.sleep(1)
    print(Fore.BLUE+f"hi {player_name}, nice to meet you!")
    time.sleep(1)
    favourite_animal = input(Fore.CYAN+"What's your favourite animal? ")
    time.sleep(1)
    print(Fore.LIGHTRED_EX+f"Awww, {favourite_animal}'s are extremely cute!")

show = introduction()