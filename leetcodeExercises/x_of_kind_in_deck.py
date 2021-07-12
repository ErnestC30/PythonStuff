"""
In a deck of cards, each card has an integer written on it.
Return true if and only if you can choose X >= 2 such that it is possible to split the entire deck 
into 1 or more groups of cards, where:
Each group has exactly X cards.
All the cards in each group have the same integer.
Input: deck = [1,2,3,4,4,3,2,1]
Output: true
Explanation: Possible partition [1,1],[2,2],[3,3],[4,4].
"""

def hasGroupSizeX(deck):
    occurences = {}
    leastOccurences = 0

    if len(deck) == 1:
        return False
    
    for val in deck:                                    #Build dictionary for occurences of each value
        if val not in occurences:
            occurences[val] = 1
        else:
            occurences[val] += 1

    for occurence in list(occurences.values()):         #Find the minimum occurence of all occurences
        if leastOccurences == 0: 
            leastOccurences = occurence
        if leastOccurences > occurence:
            leastOccurences = occurence

    divisible = True
    for occurence in list(occurences.values()):          #Check if all occurences are divisible by least occurences to form groups
        if occurence % leastOccurences != 0:
            divisible = False
    
    return divisible


deck = [1,2,3,4,4,3,2,1]
print(hasGroupSizeX(deck))

deck = [1,1,1,2,2,2,3,3]
print(hasGroupSizeX(deck))

deck = [1]
print(hasGroupSizeX(deck))

deck = [1,1]
print(hasGroupSizeX(deck))


