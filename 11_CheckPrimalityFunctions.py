"""
Exercise 11 - Check Primality Functions
Level - X X X

Ask the user for a number and determine whether the number is prime or not.
"""

def isPrime(number):
    for x in range(2, number):
        if number % x == 0:
            return("not prime :(")
    return("Prime!!! PagChomp")
number = int(input("Enter a number: "))

print(isPrime(number))
        
