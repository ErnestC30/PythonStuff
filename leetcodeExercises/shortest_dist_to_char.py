"""
Given a string s and a character c that occurs in s, return an array of integers answer where 
answer.length == s.length and answer[i] is the distance from index i to the closest occurrence of character c in s.
The distance between two indices i and j is abs(i - j), where abs is the absolute value function.

Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]
"""

def shortest_dist(s, c):
    #Pass through the list twice (once forward, once reversed), finding the minimum distance to each 'c' from each direction
    n = len(s)
    shortest = [n] * n
    pos = -n
    for i in list(range(n)) + list(range(n)[::-1]):     #Iterate from 0 to n to 0
        if s[i] == c:
            pos = i                                     #Update the new pos of 'c' to compare values to
        shortest[i] = min(shortest[i], abs(i-pos))      #Use the minimum distance of the forward/reverse run

    return shortest

s = "loveleetcode"
c = "e"
print(shortest_dist(s, c))

s = "aaab"
c = "b"
print(shortest_dist(s, c))

