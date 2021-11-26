import re
from bs4 import BeautifulSoup
from urllib.request import urlopen

url = 'https://letterboxd.com/z_rebecca/films/diary/for/2020/'
html = urlopen(url)
soup = BeautifulSoup(html, "lxml")

# print(soup.find_all('h2'))
heading = soup.find_all('h2')[0].text
print(heading.split()[3]) # Header format: [account] has logged [num] entries for films in 2020
