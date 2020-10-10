#Musixmatch scraper
#by https://github.com/podato
import requests
import sys
import re
from bs4 import BeautifulSoup


if len(sys.argv) == 1:
    url = input("Song URL: ")
elif len(sys.argv) == 2:
    url = sys.argv[1]

print("Retrieving html")
page = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"})
print("Creating soup")
soup = BeautifulSoup(page.content, 'html.parser')
print("Filtering")
results = soup.findAll(class_="lyrics__content__ok", text=True)
lyrics = results[0].get_text() + "\n" + results[1].get_text()
title = soup.find('title').get_text()[:-20]
print("Writing to file")
with open(f"{title}.txt", "w") as f:
    f.write(lyrics)

print(f'''
Successfully scraped the lyrics of: {title}
and saved to {title}.txt
''')
