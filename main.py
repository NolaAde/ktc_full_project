# Import dependencies
# A dependency is a libary or module that our code needs to function
from ast import Assert
import time #to make the code interactive from
from colorama import Fore, Style, init # color text on the terminal

#launch  coloroma
init(autoreset = True)

player_score = 0

def introduction():
    # Welcome the player
    print(Fore.LIGHTMAGENTA_EX+"Welcome to python adventure")
    time.sleep(2)
    player_name = input(Fore.GREEN + "What's your name?")
    time.sleep(2)
    print(f"hi {player_name}, nice to meet you! I'm Horimi. I am your guide and will help you through the game.")
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

def forest_path():
    print(Fore.LIGHTMAGENTA_EX+"You come across a fork in the path")
    time.sleep(5)
    choice = make_choice("Which route will you choose", ["Go left", "Go right"], [1, -1])

    if choice == 1:
        print(Fore.LIGHTCYAN_EX + "You encounter a friendly cat and she leads the way to the next challenge")
    else:
        print(Fore.LIGHTBLUE_EX + "Oh no, you encountered a venomous spider and you are trapped in his web")
time.sleep(5)
def mountain_climb():
    print("You continue to were you are headed and reach a steep mountain.")
    time.sleep(5)
    choice = make_choice( "what do you do?", ["Use a rope", "Climb without equipment."], [1, -1])

    if choice == 1:
        print(Fore.CYAN + "Smart. Using a rope makes it easier to climb")
    else:
        print(Fore.BLUE + "No, you were supposed to use the rope! You slipped but Horimi saved you, lucky you.")
time.sleep(2)
def mystical_cave():
    print(Fore.LIGHTMAGENTA_EX + "After that adventure, i think you might enjoy resting in a magical cave.")
    time.sleep(5)
    choice = make_choice(Fore.LIGHTGREEN_EX + "what do you do?", ["Explore the cave", "Just rest and then leave without exploring"], [1, -1])
    time.sleep(2)
    if choice == 1:
        print(Fore.CYAN + "Wow, you got the power of moving things with your mind")
    else:
        print(Fore.BLUE + "Horimi said you could have gotten powers. You turn back to face the cave but it disapeared, poor you.")
# Main game loop
def play_game():
    introduction()

    # Start of the adventure
    forest_path()
    mountain_climb()
    mystical_cave()
    
if __name__ == "__main__":
        play_game()