"""
You are given a string allowed consisting of distinct characters and an array of strings words.
A string is consistent if all characters in the string appear in the string allowed.
Return the number of consistent strings in the array words.
"""

def consistent_string(allowed, words):

    c_strings = 0
    for word in words:
        consistent = True
        for char in word:
            if char not in allowed:
                consistent = False

        if consistent:
            c_strings += 1

    return c_strings

allowed = "abc"
words = ["a","b","c","ab","ac","bc","abc"]
print(consistent_string(allowed, words))
