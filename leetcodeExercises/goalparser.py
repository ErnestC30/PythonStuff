"""
You own a Goal Parser that can interpret a string command. 
The command consists of an alphabet of "G", "()" and/or "(al)" in some order. 
The Goal Parser will interpret "G" as the string "G", "()" as the string "o", and "(al)" as the string "al". 
The interpreted strings are then concatenated in the original order.
Given the string command, return the Goal Parser's interpretation of command.
"""
import re

def goalparser(str):
    return re.sub('\(\)', 'o', re.sub('\(al\)', 'al', str))


command = "G()(al)"
command1 = "(al)G(al)()()G"

print(goalparser(command))
print(goalparser(command1))