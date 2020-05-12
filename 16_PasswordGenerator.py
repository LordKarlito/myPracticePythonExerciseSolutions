"""
Exercise 15: Reverse Word Order
Level: X X X X

Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols. The passwords should be random, generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:
Ask the user how strong they want their password to be. For weak passwords, Pick a word or two from a list.
"""
import random
import time

def genPassword(length, pwStrength):
    start_time = time.time()
    password = ""
    if pwStrength == 1:
        passwordList = [chr(random.randrange(97,122)) for x in range(0,length)]
        password = "".join(passwordList)        
        return(password + " program executed in {}ms".format(time.time() - start_time))

    elif pwStrength == 2:
        for x in range(0,length):
            roll = random.randint(0,1)
            if roll == 0:
                char = chr(random.randrange(97,122))  
                password = password + char
            elif roll == 1:
                char = chr(random.randrange(65,90))  
                password = password + char

        return(password + " program executed in {}ms".format(time.time() - start_time))

    elif pwStrength == 3:
        for x in range(0,length):
            roll = random.randint(0,2)
            if roll == 0:
                char = chr(random.randrange(97,122))  
                password = password + char
            elif roll == 1:
                char = chr(random.randrange(65,90))  
                password = password + char
            elif roll == 2:
                char = chr(random.randrange(48,57))  
                password = password + char
        return(password + " program executed in {}ms".format(time.time() - start_time))

    elif pwStrength == 4:
        passwordList = [chr(random.randrange(21,126)) for x in range(0,length)]
        password = "".join(passwordList)        
        return(password + " program executed in {}ms".format(time.time() - start_time))


def userInput():
    length = int(input("How many characters? "))
    pwStrength = int(input("How strong do you want your password to be? [1] - Weak [4] - Strong "))

    return(genPassword(length, pwStrength))

print(userInput())