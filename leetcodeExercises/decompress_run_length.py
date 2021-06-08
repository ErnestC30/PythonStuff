"""
We are given a list nums of integers representing a list compressed with run-length encoding.
Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).  
For each such pair, there are freq elements with value val concatenated in a sublist.
Concatenate all the sublists from left to right to generate the decompressed list.
Return the decompressed list.
"""


def decompress(nums):
    decompressed_lst = []
    for i in range(len(nums)//2):
        freq, val = nums[2*i], nums[2*i+1]
        new_vals = [val] * freq
        decompressed_lst += new_vals
    
    return decompressed_lst

nums = [1,2,3,4,5,6]
print(decompress(nums))

