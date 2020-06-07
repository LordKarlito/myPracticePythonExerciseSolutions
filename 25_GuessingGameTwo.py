"""
Exercise 25 - Guessing Game Two
Level - X X X

In a previous exercise we've written a program that "knows" a number and asks a user to guess it.

This time, we're going to do exactly the opposite. You, the user, will have in your head a number between 0 and 100. The program will guess a number, and you, the user, will say whether it's too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took to get your number.

As the writer of this proram, you will have to choose how your program will strategically guess. A naive strategy can be to simply start the guessing at 1, and keep going (2,3,4, etc.) until you hit the number. But that's not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range), and then increase/decrease by 1 as needed. After you've written the program, try to find the optimal strategy!
"""

def guess():
    num = 50
    correct = False

    while correct == False:
        firstguess = input("is your number {}?[Y/N]".format(num)).capitalize()
        if firstguess == 'Y':
            return("nice")
            correct = True

        elif firstguess == 'N':
            compare = input("Is your number less than or greater than {}? [</>]".format(num))

            if compare == '<':
                num -= 1
            elif compare == '>':
                num += 1

if input("Do you have a number between 0-100 in your mind? [Y/N]").capitalize()=='Y':
    print(guess())

else:
    print("Come back next time if you have a number! >:(")

# Another solution for this is to use binary search. But that's an exercise for another day :)