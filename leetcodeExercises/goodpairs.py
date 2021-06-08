"""
Given an array of integers nums.
A pair (i,j) is called good if nums[i] == nums[j] and i < j.
Return the pairs of indices that are good pairs.
"""

def goodpairs(nums):
    pairs = []
    for i in range(len(nums)-1):
        j = i + 1
        for j in range(i+1,len(nums)):
            if nums[i] == nums[j]:
                pairs.append((i, j))
    return pairs

nums = [1,2,3,1,1,3]
print(f'The following pairs of indices are good pairs: {goodpairs(nums)}')

    

