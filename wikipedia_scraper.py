"""
Creating a way to scrape wikipedia articles using the 'requests' and 'beautifulsoup' library.
Able to visit a random or selected Wikipedia page, then find occurences of specified words.
Things that could be added:
    More input checking
    Use wikipedia search function to get a page
    Find most common words in the page
"""

import requests
from bs4 import BeautifulSoup

def get_input():
    #Returns user's input
    print('')
    print("Enter '1' to navigate to a random wikipedia page.")
    print("Enter '2' to enter your own wikipedia url page.")
    print("Enter '3' to find occurences of words on the current wikipedia page.")
    print("Enter '4' to close the program.")
    return input()

def open_page(url='https://en.wikipedia.org/wiki/Special:Random'):
    #Returns a beautifulsoup object containing all html elements in the url.
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    return soup

def get_text(soup):
    #Returns all text in the beautifulsoup object.
    return soup.get_text(" ", strip=True)

def get_title(soup):
    #Returns the title of the page.
    return soup.title.string[:-12]
    
def find_occurence(text, targets):
    #Returns the number of times each target word appears in the text as a list
    #Targets taken as a list of strings
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
    running = True
    soup = ''
    print("Welcome to the Wikipedia web scraper tool.")
    while running:
        selection = get_input()

        if selection == '1':
            #Visit a random Wikipedia page.
            soup = open_page()
            print(f"The randomly selected Wikipedia page is the '{get_title(soup)}' page.")
    
        if selection == '2':
            #Visit a specified Wikipedia page.
            print("Enter a Wikipedia url link.")
            url = input('')
            soup = open_page(url)
            print(f"Now visiting the '{get_title(soup)}' page.")

        if selection == '3':
            #Find occurences of a list of words on the current Wikipedia page.
            if not isinstance(soup, BeautifulSoup):
                print("Need to go to a random or selected Wikipedia page first.")
                continue

            print(f"You are now accessing the '{get_title(soup)}' page.")
            print('Enter words that you want to search for, separated by spaces.')
            words = input()
            targets = words.split()
            find_occurence(soup.get_text(), targets)            

        if selection == '4':
            #Close program
            running = False



if __name__ == '__main__':
    main()
