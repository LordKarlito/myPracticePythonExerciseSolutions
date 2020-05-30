"""
Exercise 19: Decode A Web Page Two
Level: X X X X

Using the requests and BeautifulSoup Python libraries, print to the screen the full text of the article on this website: http://www.vanityfair.com/society/2014/06/monica-lewinsky-humiliation-culture.
The article is long, so it is split up between 4 pages. Your task is to print out the text to the screen so that you can read the full article without having to click any buttons.

(Hint: the post here describes in detail how to use the beautifulsoup and requests libraries through the solution of the exercise posted here.)

This will just print the full text of the article to the screen. It will not make it easy to read, so the next exercise we will learn how to write this text to a .txt file.
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
for i in p_tags:
    print(i)
    print("===")