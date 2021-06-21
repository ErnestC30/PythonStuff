"""
Creating a way to scrape wikipedia articles using the 'requests' and 'beautifulsoup' library.
Things to add:
    Navigate through specificly given urls or access a random article
    Count occurence of word
    Get title of page
"""

import requests
from bs4 import BeautifulSoup

def open_page(url):
    #Returns a beautifulsoup object containing all html elements in the url.
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_text(soup):
    #Returns all text in the beautifulsoup object.
    return soup.get_text(" ", strip=True)

def get_header(soup):
    #Returns the header of the page.
    return soup.title.string[:-12]
    
def find_occurence(text, *targets):
    #Returns the number of times each target word appears in the text as a list
    words = text.split()
    count = {}

    for word in words:
        if word in count:
            count[word] += 1
        else:
            count[word] = 1

    for target in targets:
        if target in count:
            print(f'The amount of times {target} appears in the text is: {count[target]}')
        else:
            print(f'The amount of times {target} appears in the text is: 0')
   
def main():
    pass

url = 'https://en.wikipedia.org/wiki/Special:Random'
soup = open_page(url)
text = get_text(soup)
print(get_header(soup))

#find_occurence(text, 'League', 'the', 'Rift')
