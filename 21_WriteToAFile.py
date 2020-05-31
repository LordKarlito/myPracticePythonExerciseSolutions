"""
Exercise 21 - Write To A File
Take the code from the How To Decode A Website exercise (if you didn’t do it or just want to play with some different code, use the code from the solution), and instead of printing the results to a screen, write the results to a txt file. In your code, just make up a name for the file you are saving to.

Extras:

Ask the user to specify the name of the output file that will be saved.
"""

# Import needed libraries
import requests
from bs4 import BeautifulSoup

# Get the html
r = requests.get("https://www.vanityfair.com/style/society/2014/06/monica-lewinsky-humiliation-culture")
r_html = r.content

# Make some soup :)
soup = BeautifulSoup(r_html, features='html.parser')

# Initialize the array where the paragraphs will be stored
p_tags = []

# All paragraphs are stored in div elements with class "grid--item body body__container article__body grid-layout__content". Let's find all of them.
for div_tag in soup.find_all("div", {"class": "grid--item body body__container article__body grid-layout__content"}):
    
    # Within these div tags are multiple p tags that we want to get. So for this let's use find_all.
    for p_tag in div_tag.find_all("p"):

        # Append that shit to the array.
        p_tags.append(p_tag.text)


# Print the result to see the fruits of our labor. :'D
# for i in p_tags:
#     print(i)
#     print("===")

string = "\n".join(p_tags)

filename = input("Enter output filename: ")

with open(filename, 'w') as open_file:
    open_file.write(string)