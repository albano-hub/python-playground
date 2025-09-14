# Addind a comment line to practice using git
import time
import shutil 
from time import sleep

# Constants
screen_width = shutil.get_terminal_size().columns
SLEEP_SPACE = 0.1
SLEEP_PERIOD = 0.5
SLEEP_COMMA = 0.3
SLEEP_CHAR = 0.02
SLEEP_SPAUSE = 0.5

# Functions
def clear_console():
    print("\033[H\033[J")  # Clear the console (may not work in all environments)

def print_title():
    print(' My First Game '.center(29, '*').center(screen_width))

def twprint(O_str):
    for char in O_str:
        print(char, end='', flush=True)
        if char == " ":
            sleep(SLEEP_SPACE)  # Slightly longer delay for spaces
        elif char == ".":
            sleep(SLEEP_PERIOD)  # Longer delay for periods
        elif char == ",":
            sleep(SLEEP_COMMA)  # Medium delay for commas
        else:
            sleep(SLEEP_CHAR)

# User info input
def get_user_info():
    twprint("What is your name?\n -")
    name = input()
    sleep(SLEEP_SPAUSE) 
    while True:
        twprint("How old are you?\n -")
        try:
            age = int(input())
            break
        except ValueError:
            twprint("Please enter a valid number for age.\n")
    sleep(1)
    return name, age    

#Main game loop function code
def game_loop(name, age):
    str1 = "Hello"+" "+ name +", you are "+ str(age) +" years old! "
    twprint(str1)
    sleep(SLEEP_SPAUSE)

    # Age test & code for choices
    if age >= 18:
        twprint("You are old enough to play.\n")
        print("\n", end='\t')
        sleep(1)
        twprint("Do you want to play? (yes/no) \n -")
        want_to_play = input().lower()
        if want_to_play == "yes":
            sleep(1.5)
            twprint("\nGreat. Let's play!\n\n")
            sleep(2)
            clear_console()
            sleep(1.25)
            twprint("Your journey begins. You are in a dark room. There is a door to your left and right. Which one do you take? (left/right) \n -I go ")
            L_R = input().lower()
            if L_R == "left":
                sleep(1)
                twprint("\nThe bright sunlight hurts your eyes as you open the door. With a deep breath you can smell the aroma of grass.")
                sleep(1)
                twprint("\nYou walk down the road and meet a stranger selling candies. Would you like to buy one? (yes/no) \n -")
                ans = input().lower()
                if ans == "yes":
                    sleep(1)
                    twprint("\nYou bought a candy and it was delicious! You win!\n")
                    sleep(2)
                    print(" ;-) \n")
                    sleep(2)
                    # quit()
                else:
                    sleep(1)
                    twprint("\nYou ignored the stranger and walked away. Suddenly, you fell into a hole. Game over!\n")
                    sleep(2)
                    print(" ;-) \n")
                    sleep(2)
                    # quit()
            else:
                sleep(1)
                twprint("\nYou enter a room full of snakes. They look hungry and one of them bites you. Game over!\n")
                sleep(2)
                print(" ;-) \n")
                sleep(2)
                # quit()
        else:
            sleep(1)
            twprint("Maybe next time.\n")
            print("\n ;-) \n")
            sleep(2)
            # quit()    
    else:
        sleep(1.25)
        twprint("Unfortunately, you are not old enough to play.\n")
        sleep(1)
        print("Maybe next time.\n")
        sleep(SLEEP_SPAUSE)
        print(" ;-) \n")
        sleep(3)

# Intro page
def main():
    clear_console()
    print()
    print_title()
    sleep(SLEEP_SPAUSE)
    twprint("\n\nWelcome to my first game! ")
    sleep(1)
    twprint("In this game, you will be able to make choices and see how they affect the outcome of the game.\n")
    twprint("Let's start with getting to know each other.\n")
    input()
    clear_console()
    print()
    print_title()
    sleep(SLEEP_SPAUSE)
    print("\n\n")
    name, age = get_user_info()
    game_loop(name, age)

if __name__ == "__main__":
    main()
