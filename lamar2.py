from bs4 import BeautifulSoup
import requests

studyLink = requests.get('https://sneakernews.com/release-dates/').text

Sneaker = BeautifulSoup(studyLink, 'html.parser')

h2s = Sneaker.findAll("h2")
releaseDate = Sneaker.findAll("span", {"class": "release-date"})

h1 = Sneaker.find("h1")

print("Page Title:", h1.text.strip(), end="\n\n")


counter = -2
total = 0

for h2 in h2s:
    if counter < 0:
        counter+=1
        continue
    
    counter += 1
    print("Sneaker No. ", counter, ": ", h2.text.strip(), sep="")
    
    for date in releaseDate:
        total += 1
        if counter == total:
            print("Release Date for Sneaker No. ", counter, ": ", date.text.strip(), sep="")
            print()
        else:
            continue
    total = 0


