"""
Write a program that converts a word into morse code.
"""

def convert_to_morse(word):
    #List containing the morse code for letters a-z
    morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",\
                 ".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--",\
                 "-..-","-.--","--.."]

    code = ''
    for char in word:
        code += morse_code[ord(char) - ord('a')]
    
    return code
        

word = 'dog'
print(convert_to_morse(word))

word2 = 'watermelon'
print(convert_to_morse(word2))