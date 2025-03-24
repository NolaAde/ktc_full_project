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
    player_name = input(Fore.CYAN+"What's your name?")
    time.sleep(1)
    print(Fore.BLUE+f"hi {player_name}, nice to meet you!")
    time.sleep(1)
    favourite_animal = input(Fore.CYAN+"What's your favourite animal? ")
    time.sleep(1)
    print(Fore.LIGHTRED_EX+f"Awww, {favourite_animal}'s are extremely cute!")
    print(Fore.LIGHTMAGENTA_EX+f"Come on an adventure with me!")
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

def Breakfast():
    print(Fore.LIGHTMAGENTA_EX+"You come across a fork in what to eat")
    time.sleep(5)
    choice = make_choice("On one plate, there is your favourite food, and on the second plate there is your second favourite food. Which one do you choose?", ["Plate a", "Plate b"], [1, -1])

    if choice == 1:
        print(Fore.LIGHTCYAN_EX + "OH NO! Your favourite food is filled with a sleep potion.")
    else:
        print(Fore.LIGHTBLUE_EX + "You were fine and make your way to climb a mountain......buuut you nocked out by some passers by.")
time.sleep(5)
def mountain_climb():
    print(Fore.LIGHTMAGENTA_EX+"You wake up in front of a steep mountain.")
    time.sleep(1)
    choice = make_choice(Fore.LIGHTMAGENTA_EX+"what do you do?", ["Use a rope", "Climb without equipment."], [1, -1])

    if choice == 1:
        print(Fore.CYAN + "Smart. Using a rope makes it easier to climb")
    else:
        print(Fore.BLUE + "No, you were supposed to use the rope! You slipped but Nikki saved you, lucky you.")
time.sleep(2)
def mystical_cave():
    print(Fore.LIGHTMAGENTA_EX + "After that adventure, i think you might enjoy resting in a magical cave.")
    time.sleep(5)
    choice = make_choice(Fore.LIGHTGREEN_EX + "what do you do?",["Explore the cave", "Just rest and then leave without exploring"], [1, -1])
    time.sleep(2)
    if choice == 1:
        print(Fore.CYAN + "Wow, you got the power of moving things with your mind")
    else:
         print(Fore.BLUE + "Nikki said you could have gotten powers. You turn back to face the cave but it disapeared, poor you.")

def river_crossing():
    print(Fore.LIGHTMAGENTA_EX + "There is a wide, rushing river blocking your way")
    time.sleep(5)
    choice = make_choice(Fore.LIGHTGREEN_EX + "what do you do?",["make a raft", "swim across"], [1, -1])
    time.sleep(2)
    if choice == 1:
        print(Fore.CYAN + "You get there safely")
    else:
         print(Fore.BLUE + "You somehow managed to survive with many injuries but Nikki healed you.")

def hidden_treasure():
    print(Fore.LIGHTMAGENTA_EX + "Finally, you reach a massive treasure box")
    time.sleep(5)
    choice = make_choice(Fore.LIGHTGREEN_EX + "what do you do?",["open it", "Leave it"], [1, -1])
    time.sleep(2)
    if choice == 1:
        print(Fore.CYAN + "The treasere you found was trilions of pounds, you take them home with you happily and save it")
    else:
         print(Fore.BLUE + "Nikki said the treasure was in there. You turn to get it but some theifs stole it.You didn't care and made your way back home.")
    print(Fore.BLUE + "Nikki gives you a crown and says'Your Majesty'.")

# Main game loop
def play_game():
    introduction()

    # Start of the adventure
    Breakfast()
    mountain_climb()
    mystical_cave()
    river_crossing()
    hidden_treasure()
if __name__ == "__main__":
        play_game()