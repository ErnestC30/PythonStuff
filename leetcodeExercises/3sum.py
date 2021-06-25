"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
and nums[i] + nums[j] + nums[k] == 0.
Notice that the solution set must not contain duplicate triplets.
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
"""

def threesums(nums):
    l = 0               #Pointers to compare triplets
    m = 1
    r = 2

    sum_to_0 = []
    last_index = len(nums) - 1
    comparing = True

    if nums == None or len(nums) < 3:
        return []

    while comparing:
        #print(l,m,r)
        added = nums[l] + nums[m] + nums[r]
        if added == 0:
            duplicate = False      #Ignore duplicate triplets by comparing values as a set
            for triplet in sum_to_0:                 
                if set(triplet) == set([nums[l], nums[m], nums[r]]):
                    duplicate = True
            if not duplicate:
                sum_to_0.append([nums[l], nums[m], nums[r]])

        r += 1
        if r > last_index:         #If 'r' reaches last index, then increase 'm' by 1, then reset 'r' pointer
            m += 1
            r = m + 1

        if m > last_index - 1:     #If 'm' reaches the second last index, then increase 'l' by 1, then reset 'm' and 'r' pointer
            l += 1
            m = l + 1
            r = m + 1

        if l > last_index - 2:     #When 'l' is at the third last index, then all possible triplets have been considered.
            comparing = False
    
    return sum_to_0


nums = [-1,0,1,2,-1,-4]
print(threesums(nums))
        
nums = [0]
print(threesums(nums))