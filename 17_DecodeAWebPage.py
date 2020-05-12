"""
Exercise 17: Reverse Word Order
Level: X X X X

Use the BeautifulSoup and requests Python packages to print out a list of all the navigation links found in the sidebar of https://www.crummy.com/software/BeautifulSoup/bs4/doc/.

"""

# Import necessary libraries
import requests
from bs4 import BeautifulSoup

# Get the html
url = "https://www.crummy.com/software/BeautifulSoup/bs4/doc/"
r = requests.get(url)
r_html = r.text

# yummy soup
soup = BeautifulSoup(r_html, features='html.parser')


sidebar = soup.find("div", {"class" : "sphinxsidebarwrapper"})
li = sidebar.find_all("a", {"class" : "reference internal"})

for link in li:
    print(link.text)