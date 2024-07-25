# Import dependencies
# A dependency is a libary or module that our code needs to function
from random import choice
import time #to make the code interactive from
from colorama import Fore, Style, init # color text on the terminal

#launch coloroma
init(autoreset = True)

player_score = 0

def introduction():
    # Welcome the player
    print(Fore.LIGHTMAGENTA_EX+"Good Morning sunshine!!!!!!!!!")
    time.sleep(2)
    player_name = input(Fore.GREEN + "What's your name?: ")
    time.sleep(2)
    print(f"hi {player_name}, nice to meet you! I'm Noala. I am your guide, do you remember me from the other python game. yea python adventure.")
    time.sleep(2)

def make_choice(question, options, score_change):
    print(question)
    for i, option in enumerate(options, 1):
        print(f"{i}. {option}")
    while True:
        try:
            choice = int(input("Enter the number of your choice: "))
            if 1 <= choice <= len(options):
                # update global score variable
                global player_score 
                player_score += score_change[choice - 1]
                return choice
            else:
                print("Invalid choice try again")
        except ValueError:
            print("invalid input. Enter a number")

def wake_up():
    print(Fore.LIGHTMAGENTA_EX+"You wake up on christmas day and realised you over slept")
    time.sleep(2)
    choice = make_choice("What do you do?", ["check your alarm clock", "rush to make it on time to were you are headed."], [1, -1])

    if choice == 1:
        print(Fore.LIGHTCYAN_EX + "You still had an extra 2 hours to get ready. Good for you.")
    else:
        print(Fore.LIGHTBLUE_EX + "Noala had to make you sleep for 1 hour because you were acting crazy.")

def breckky():
    print("You need some brecky. You need something to hold your belly because you are going to barry_island so you will definetly eat there")
    choice = make_choice("wat u munching",["Cereal", "Plantain and egg"], [1, -1])
    
    if choice == 1:
        print("Good you are not full but this is enough to hold your belly and its quick to make.")
    else:
        print("its to long. you have 1:30(1 hour 30 minutes)until barry island closes, now you are gonna be late.")
        time.sleep(2)
def barry_island():
    print(Fore.LIGHTMAGENTA_EX+"You realised that barry_island was privately booked and you cant enter.")
    time.sleep(2)
    choice = make_choice(Fore.LIGHTMAGENTA_EX+"what do you do?", ["Complain to the authorities", "go to winter wonderland"], [1, -1])
    if choice == 1:
        print(Fore.CYAN + "The authorities could not do anything because the king was the one who did that.")
    else:
        print(Fore.BLUE + "Wow, Noala had privately booked winter wonder land for you and your friends and family.")
time.sleep(2)
def winter_wonderland():
    print(Fore.LIGHTMAGENTA_EX + "You go to winter wonder land and when you did, you were enjoying yourself and you see a scary ride")
    time.sleep(2)
    choice = make_choice(Fore.LIGHTGREEN_EX + "what do you do?",["Go on the ride", "dont go on it"], [1, -1])
    time.sleep(2)
    if choice == 1:
        print(Fore.CYAN + "You remembered you hated scary things so Noala had to teleport you out of the ride and makes you forget about the ride.")
    else:
        print(Fore.BLUE + "Good because you remembered you hated scary stuff.")

def presents():
    print(Fore.CYAN + "Its time to open some christmas but there was a catch, you could only open two presents.")
    choice = make_choice(Fore.CYAN + "Which pair shall you choose?", ["pair a", "pair b"], [1, -1])
    if choice == 1:
        print(Fore.CYAN + "You got all the presents and a bottle of perfume with a nintendo.")
    else:
        print(Fore.CYAN + "You got sonic figurines and your own house and car")
    print(Fore.CYAN + "Well, christmas is over...........buuuuuuuut you remembered your bestie's birthday party is in 10 minutes.")
def party():
# Main game loop
 def play_game():
        introduction()

    # Start of the adventure
    wake_up()
    breckky()
    barry_island()
    winter_wonderland()
    presents()
    
if __name__ == "__main__":
    play_game()