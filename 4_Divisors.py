"""
Exercise 4 - Divisors
Level - X X

Create a program that asks the user for a number then prints out a list of all the divisors of that number
"""

num = int(input("Enter a number: "))

divisors = [x for x in range(1, num+1) if (num % x == 0)]

print(divisors)