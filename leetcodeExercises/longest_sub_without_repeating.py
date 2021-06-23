"""
Given a string s, find the length of the longest substring without repeating characters.
"""

def lengthOfLongestSubstring(s):
    #Faster solution - O(n)
    dict = {}
    longest = start = 0                               #'start' is the variable where it begins counting the length of substring
    for i, c in enumerate(s):
        if c in dict and start <= dict[c]:            #If there is a duplicate value, then update 'start' value to the next index 
            start = dict[c] + 1                       #that is after the previous occurence of the repeating char
        else:
            longest = max(longest, i - start + 1)       
        dict[c] = i                                   #Store most recent index of the current char in dictionary
    return longest

def bruteLengthOfLongestSubstring(s):
    #Bruteforce solution - O(n^2)
    longest = 0
    if len(s) == 0:
        return 0

    for i in range(len(s)):
        cur_longest = 0
        dict = {}
        j = i
        while j < len(s) and s[j] not in dict:
            dict[s[j]] = 1
            cur_longest += 1
            j += 1
        if cur_longest > longest:
            longest = cur_longest
    
    return longest
        
s = "abcabcbb"
print(lengthOfLongestSubstring(s))

s = "abcdefdghdidjklmnopqrs"
print(lengthOfLongestSubstring(s))
