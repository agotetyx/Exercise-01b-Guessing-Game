import sys, random
assert sys.version_info >= (3,8), "This script requires at least Python 3.8"

import random

number = random.randint(1,10)
num = str (number)
tries = 5
guessCount = 0
print ("You have 5 chances")
guess = input("Guess a number from 1 to 10: ")
while guessCount != tries-1:
    print
    if guess in "qwertyuiopcvbnmZXCVBNMQWERTYUIOPasdfghjklASDFGHJKLzx":
        print("Choose ONLY between 1-10")
        guess = input("Guess a number from 1 to 10: ")
        guessCount+=1
    else:
            if int(guess) < number:
                print("Too low. Try again. ")
                guessCount+=1
                guess = input("Guess a number from 1 to 10: ")
            elif int(guess) > number:
                print("Too high. Try again. ")
                guessCount+=1
                guess = input("Guess a number from 1 to 10: ")
            elif int(guess)==number:
                print("Right answer!")
                break

if guessCount == 4:
    print("FAIL. Out of tries.")
if guessCount !=tries:
    print("The number was:" + num)

