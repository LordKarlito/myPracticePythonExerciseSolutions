"""
Exercise 22 - Read From File
Level - X
Given a .txt file that has a list of a bunch of names, count how many of each name there are in the file, and print out the results to a screen. 

Extra:
Instead of using .txt file from the above (or instead of, if you want the challenge), use XXX and count how many of each "category" of each image there are. This text file is actually a list of files corresponding to the SUN database scene recognition database, and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file, it will be clear which part represents the scene category. To do this, you're going to have to remember a bit about string parsing in Python 3.
"""

"""
# Vanilla version
# Open file
with open('names.txt', 'r') as open_file:
    all_text = open_file.read()

# Split string in txt to lines
arr = all_text.split("\n")

# Initialize the dictionary
unique_dict = {}

# Get unique values and assign the value of 0
for name in arr:
    if name not in unique_dict:
        unique_dict.update({name:0})

# iterate through the txt file then increment value to count the number of times the name has been found.
for name in arr:
    unique_dict[name] += 1

print(unique_dict)
"""

# Solution for the extra challenge

#open the file
with open('listOfFiles.txt', 'r') as open_file:
    all_text = open_file.read()

#Split string into lines
arr = all_text.split('\n')
categories = [line.split('/')[2]  for line in arr]

# Get unique list of categories
unique_categories = []
for x in categories:
    if x not in unique_categories:
        unique_categories.append(x)

# Initialize Dictionary
myDict = {}

# Add unique categories to dictionary with value of 0
for x in unique_categories:
    if x not in myDict:
        myDict.update({x:0})

# Iterate through categories and increment value
for x in categories:
    myDict[x] += 1

# Show result :)
print(myDict)
