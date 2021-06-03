"""
You're given strings jewels representing the types of stones that are jewels, and stones representing the stones you have. 
Each character in stones is a type of stone you have. 
You want to know how many of the stones you have are also jewels.
Letters are case sensitive, so "a" is considered a different type of stone from "A".
"""

def jewel_and_stones(jewels, stones):
    #Sum up numbers of time a char in jewel appears in stones using a GENERATOR   
    num = [char in jewels for char in stones]
    print(num)
    print(sum(num))
    return sum(char in jewels for char in stones)


jewels = "a"
stones = "aaAAbaC"
print(jewel_and_stones(jewels, stones))


