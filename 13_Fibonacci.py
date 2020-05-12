"""
Exercise 13 - Fibonacci
Level - X X

Write a program that asks the user how many Fibonnaci numbers to geenrate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate.

Notes:
1, 1, 2, 3, 5, 8, 13, ...
sum of previous 2 numbers
"""

count = int(input("Enter how many numbers in the fibonnaci sequence: "))

def fibonnaci(count):
    fib = []
    if count == 0:
        fib = []
    elif count == 1:
        fib = [0, 1]
        del fib[0]
    elif count > 1:
        fib = [0, 1]
        for x in range(1, count):
            fib.append(fib[-2] + fib[-1])
        del fib[0]
    
    return(fib)
print(fibonnaci(count))