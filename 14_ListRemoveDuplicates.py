"""
Exercise 14 - List Remove Duplicates
Level - X X

Write a program that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

EXTRAS:
- Write two different functions to do this - one using a loop and constructing a list, and another using sets.
"""

myList = [1,1,2,3,4,12,3,1,4,5,23,2,2]

def removeDuplicatesSet(myList):
    newlist = set(myList)
    return(newlist)

def removeDuplicatesList(myList):
    newlist = []
    for x in range(len(myList)):
        if myList[x] not in newlist:
            newlist.append(myList[x])

    return(newlist)

print(removeDuplicatesSet(myList))
print(removeDuplicatesList(myList))