import os
import time
from time import sleep
import shutil

screen_width = shutil.get_terminal_size().columns

def twprint(O_str):
    for char in O_str:
        print(char, end='', flush=True)
        if char == " ":
            sleep(0.1)  # Slightly longer delay for spaces
        elif char == ".":
            sleep(0.5)  # Longer delay for periods
        elif char == ",":
            sleep(0.3)  # Medium delay for commas
        else:
            sleep(0.02)

print("\033[H\033[J")  # Clear the console (may not work in all environments)
print()
# for i in range(0, 40):
#     print(i, end='', flush=True)
#     sleep(0.01)
print(' My First Game '.center(29, '*').center(screen_width))
sleep(0.5)

print("\n\n")
twprint("Welcome to my first game! ")
sleep(1)
twprint("In this game, you will be able to make choices and see how they affect the outcome of the game.\n")
twprint("Let's start with getting to know eachother.\n")
input()
print("\033[H\033[J")  # Clear the console (may not work in all environments)
print()
print(' My First Game '.center(29, '*').center(screen_width))
sleep(0.5)
print("\n\n")

twprint("What is your name?\n -")
name = input()
sleep(0.5) 

twprint("How old are you?\n -")
age = int(input())

sleep(1)
str1 = "Hello"+" "+ name +", you are "+ str(age) +" years old! "
twprint(str1)
# print(f"Hello {name}, you are", age, "years old!")

sleep(0.5)
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
        print("\033[H\033[J")
        sleep(1.25)
        twprint("Your journey begins. You are in a dark room. There is a door to your left and right. Which one do you take? (left/right) \n -I go")
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
                quit()
            else:
                sleep(1)
                twprint("\nYou ignored the stranger and walked away. Suddenly, you fell into a hole. Game over!\n")
                sleep(2)
                print(" ;-) \n")
                sleep(2)
                quit()
        else:
            sleep(1)
            twprint("\nYou enter a room full of snakes. They look hungry and one of them bites you. Game over!\n")
            sleep(2)
            print(" ;-) \n")
            sleep(2)
            quit()
    else:
        sleep(1)
        twprint("Maybe next time.\n")
        print("\n ;-) \n")
        sleep(2)
        quit()    
else:
    sleep(1.25)
    twprint("Unfortunately, you are not old enough to play.\n")
    sleep(1)
    print("Maybe next time.\n")
    sleep(0.5)
    print(" ;-) \n")
    sleep(3)

    quit()
    