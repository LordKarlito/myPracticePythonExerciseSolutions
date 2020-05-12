"""
Exercise 9 - Guessing Game One
Level - X X X

Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right

Extras
Keep the game going until the user types 'exit'
Keep track of how many guesses the user has taken, and when the game ends, print this out.
"""

import random


def game():
    number = random.randint(0,10)
    count = 0
    endgame = False
    while endgame == False:
        guess = input("Enter your guess: ")
        count += 1
        if guess.isnumeric():
            if int(guess) > number:
                print("Too high 420 lmao")
            elif int(guess) < number:
                print("Too low not coo bruh")
            elif int(guess) == number:
                print("HOLY SHIT NO WAY PagChomp")
                print("Number of attempts: {}".format(count))
                print("Thanks for playing!")
                endgame = True

game()