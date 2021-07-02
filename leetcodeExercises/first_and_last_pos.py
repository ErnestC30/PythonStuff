"""
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.
If target is not found in the array, return [-1, -1].
You must write an algorithm with O(log n) runtime complexity.
"""
#O(n) method
def searchRangeOn(nums, target):
    start = end = -1
    targetFound = False
    for i in range(len(nums)):
        if nums[i] == target and not targetFound:
            start = i
            targetFound = True
        if nums[i] == target and target:
            end = i

    return [start, end]

#O(logN) method
def searchRange(nums, target):
    if not nums:
        return [-1, -1]

    return [bisectLeft(nums, target), bisectRight(nums, target)]
    
def bisectLeft(nums, target):
    """Finds the smallest index of the target value"""
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r)//2
        if nums[m] < target:                #If midpoint value is less than the target, then only need to search right half of list.
            l = m + 1
        else:                               #If nums[m] is equal or greater than target, then need to shift right half of list
            r = m                           #to search for the smallest index of target.
    return l if nums[l] == target else -1   

def bisectRight(nums, target):
    """Finds the largest index of the target value"""
    l, r = 0, len(nums) - 1
    while l < r:
        m = (l + r)//2 + 1
        if nums[m] > target:
            r = m - 1
        else:
            l = m
    return l if nums[l] == target else -1


nums = [5,7,7,8,8,10] 
target = 8
print(searchRange(nums, target))


nums = [5,7,7,8,8,10]
target = 6
print(searchRange(nums, target))
