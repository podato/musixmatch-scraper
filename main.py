#Musixmatch scraper
#By https://github.com/podato
import requests
import sys
from bs4 import BeautifulSoup


out = "{title}.txt"
if len(sys.argv) == 1:
    url = input("Song URL: ")
    out = input("Output file (leave blank for default): ")
elif len(sys.argv) == 2:
    url = sys.argv[1]
elif len(sys.argv) == 3:
    url = sys.argv[1]
    out = sys.argv[2]
else:
    print(f"Expected 2 or less arguments but recieved {len(sys.argv)-1}. Remember to surround arguments containing spaces with \"\" or ''")
    exit()
if out == "":
    out = "{title}.txt"


print("Retrieving html")
page = requests.get(url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36"})

print("Creating soup")
soup = BeautifulSoup(page.content, 'html.parser')

print("Filtering")
lco = soup.findAll(class_="lyrics__content__ok", text=True)
if len(lco) > 0:
    lyrics = "\n".join(x.text for x in lco)
else:
    lyrics = soup.find(class_="lyrics__content__warning", text=True).get_text()
raw_title = soup.find('title').get_text()[:-20]

print("Writing to file")
for char in ['<', '>', ':', '"', '/', '\\', '|', '?', '*']:
    title = raw_title.replace(char, "")
with open(out.format(title=title), "w", encoding='utf8') as f:
    f.write(lyrics)

print(f'''
Successfully scraped the lyrics of: {raw_title}
and saved to: {title}.txt''')
