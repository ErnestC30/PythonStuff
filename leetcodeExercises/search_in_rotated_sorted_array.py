"""
There is an integer array nums sorted in ascending order (with distinct values).
Prior to being passed to your function, nums is rotated at an unknown pivot index k (0 <= k < nums.length)
such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
Given the array nums after the rotation and an integer target, return the index of target if it is in nums, 
or -1 if it is not in nums.
You must write an algorithm with O(log n) runtime complexity.
"""


def search(nums, target):
    length = len(nums)
    l, m, r = nums[0], nums[length//2], nums[length - 1]

    if target < l and target > r:                        #target is definitely not in the list.
        return -1

    if m > l and m > r:                                  #CASE 1: midpoint is higher value than left and right value. 
        if target < m and target >= l:                   #if target is smaller than m and larger than l, then search left half of nums.
            for i in range(length//2):
                if nums[i] == target:
                    return i                    
            else:
                return -1

        else:
            for i in range(length//2, length):           #search right half of nums otherwise.
                if nums[i] == target:
                    return i
            else:
                return -1

    else:                                                #CASE 2: midpoint is lower value than the left and right value.
        if target > m and target <= r:                   #if target is larger than m and smaller than r, then search right half of nums.
            for i in range(length//2, length):
                if nums[i] == target:
                    return i
            else:
                return -1

        else:
            for i in range(length//2):                   #search left half of nums otherwise.
                if nums[i] == target:
                    return i
            else:
                return -1


#CASE 1
nums = [5,6,7,8,9,1,2,3,4]
target = 3
print(search(nums,target))

#CASE 2
nums = [6,7,8,9,1,2,3,4,5]
target = 5
print(search(nums,target))
