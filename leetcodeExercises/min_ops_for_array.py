"""
You are given an integer array nums (0-indexed). 
In one operation, you can choose an element of the array and increment it by 1.
Return the minimum number of operations needed to make nums strictly increasing.
An array nums is strictly increasing if nums[i] < nums[i+1] for all 0 <= i < nums.length - 1. 
An array of length 1 is trivially strictly increasing.
"""

def min_increasing_array(nums):
    cur_max = 0
    ops = 0
    for num in nums:
        if num > cur_max:
            cur_max = num
        else:
            #Find the amount needed to make current num greater than the current max
            diff = cur_max - num
            num += diff + 1
            ops += diff + 1
            cur_max += 1

    return ops

nums = [1,1,1]
print(min_increasing_array(nums))
    
nums2 = [1,5,2,4,1]
print(min_increasing_array(nums2))