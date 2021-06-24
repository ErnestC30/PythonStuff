"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows like this: 
(you may want to display this pattern in a fixed font for better legibility)

P   A   H   N
A P L S I I G
Y   I   R
And then read line by line: "PAHNAPLSIIGYIR"

"""

def convert(s, rows):
    if len(s) == 1 or rows == 1:
        return s

    holder = [''] * rows             #Placeholder for each row of characters.
    step = 0                         #Step used to track which row the character is placed into.
    descending = True

    for i in range(len(s)):
        holder[step] += s[i]         #Add the next character to corresponding step
        
        if descending: 
            if step == rows - 1:     #If it reaches lowest row, then start ascending.
                descending = False
            else:
                step += 1
        
        if not descending:           #While ascending, decrease the step value.
            if step == 0:
                descending = True
                step += 1
            else:
                step -= 1

    return ''.join(holder)            #Combines all the rows together for the converted string.

s = "PAYPALISHIRING"
rows = 3
print(convert(s, rows))

rows = 4
print(convert(s, rows))