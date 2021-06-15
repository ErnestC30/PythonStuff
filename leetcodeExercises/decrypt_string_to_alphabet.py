"""
Given a string s formed by digits ('0' - '9') and '#' . We want to map s to English lowercase characters as follows:
Characters ('a' to 'i') are represented by ('1' to '9') respectively.
Characters ('j' to 'z') are represented by ('10#' to '26#') respectively. 
Return the string formed after mapping.
It's guaranteed that a unique mapping will always exist.
"""

def decrypt_string(s):
    #Note: letter 'a' starts from unicode 
    length = len(s)
    new_string = ""

    #If string is less than 3, only contains chars from a-i
    if length < 3:
        for i in range(length):
                new_string += chr(96 + int(s[i]))
        return new_string


    if length >= 3:
        i = 0
        while i < length:
            if  length - i >= 3 and s[i+2] == '#':
                new_string += chr(96 + int(s[i:i+2]))
                i += 3                                      #Need to skip to index after the '#'
            else:
                new_string += chr(96 + int(s[i]))
                i += 1

        return new_string



s = "10#11#12"
s2 = "12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#"

print(decrypt_string(s))
print(decrypt_string(s2))
print(decrypt_string('10#'))