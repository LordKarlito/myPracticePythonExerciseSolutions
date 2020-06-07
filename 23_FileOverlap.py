"""
Exercise 23 - File Overlap
Level - X X

Given two .txt files that have lists of numbers in them, find the numbers that are overlapping. One txt file has a list of all prime numbers uner 1000, and the other txt file has a list of hapy numbers up to 1000.
"""

#open the file
with open('txt files/23_primes.txt', 'r') as open_file:
    primes = open_file.read()

with open('txt files/23_happy.txt', 'r') as open_file:
    happy = open_file.read()

listPrimes = primes.split('\n')
listHappy = happy.split('\n')

listOverlap = [x for x in listPrimes if x in listHappy]

print(listOverlap)