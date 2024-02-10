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
    print(f"hi {player_name}, nice to meet you! I'm Horimiya. I am your guide and will help you through the game.You need to find a treasure and place it in its rightful place in order to leave.")
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
    print(Fore.LIGHTMAGENTA_EX+"You continue to were you are headed and reach a steep mountain.")
    time.sleep(5)
    choice = make_choice(Fore.LIGHTMAGENTA_EX+"what do you do?", ["Use a rope", "Climb without equipment."], [1, -1])

    if choice == 1:
        print(Fore.CYAN + "Smart. Using a rope makes it easier to climb")
    else:
        print(Fore.BLUE + "No, you were supposed to use the rope! You slipped but Horimiya saved you, lucky you.")
time.sleep(2)
def mystical_cave():
    print(Fore.LIGHTMAGENTA_EX + "After that adventure, i think you might enjoy resting in a magical cave.")
    time.sleep(5)
    choice = make_choice(Fore.LIGHTGREEN_EX + "what do you do?",["Explore the cave", "Just rest and then leave without exploring"], [1, -1])
    time.sleep(2)
    if choice == 1:
        print(Fore.CYAN + "Wow, you got the power of moving things with your mind")
    else:
         print(Fore.BLUE + "Horimiya said you could have gotten powers. You turn back to face the cave but it disapeared, poor you.")

def river_crossing():
    print(Fore.LIGHTMAGENTA_EX + "There is a wide, rushing river blocking your way")
    time.sleep(5)
    choice = make_choice(Fore.LIGHTGREEN_EX + "what do you do?",["make a raft", "swim across"], [1, -1])
    time.sleep(2)
    if choice == 1:
        print(Fore.CYAN + "You get there safely")
    else:
         print(Fore.BLUE + "You somehow managed to survive with many injuries but Horimiya healed you.")

def hidden_treasure():
    print(Fore.LIGHTMAGENTA_EX + "Finally, you reach a massive treasure box")
    time.sleep(5)
    choice = make_choice(Fore.LIGHTGREEN_EX + "what do you do?",["open it", "Leave it"], [1, -1])
    time.sleep(2)
    if choice == 1:
        print(Fore.CYAN + "The treasere you found was trilions of pounds, you take them home with you happily")
    else:
         print(Fore.BLUE + "Horimiya said the treasure was in there. You turn to get it but some theifs stole it.")

def spend_or_save():
    print("When you get home with your money, you had a little think about something. It was about whether you were going to spend your money, or save it.")
time.sleep(5)
choice = make_choice("What are you going to do?", ["Save your money in a bank", "Spend your money"], [1, -1])
if choice == 1:
    print("The bank suddenly changed the amount of money you had into quintilions!")
else:
    print("You bought wallet's to store your money suddenly two thiefs stole all of your wallets, but the police caught them, lucky you.")
# Main game loop
def play_game():
    introduction()

    # Start of the adventure
    forest_path()
    mountain_climb()
    mystical_cave()
    river_crossing()
    hidden_treasure()
    spend_or_save()
if __name__ == "__main__":
        play_game()