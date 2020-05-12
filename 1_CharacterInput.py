"""
Exercise 1 - Character Input
Level - X
Create a program that asks the user to enter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
1. Add on to the previous program by asking the user for another number and printing out that many copies of the previous message.
2. Print out that many copies of the previous message on separate lines.
"""

import datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))
now = datetime.datetime.now()
years = 100 - age
message = "Hi " + name + "! You will turn 100 in " + str(years) + " years which is in the year " + str(int(now.year) + years)+ "!\n"

print(message*years)