"""
Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:
arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

Input: arr = [0,3,2,1]
Output: true
"""

def validMountainArray(arr):
    isMountain = True
    isIncreasing = True

    if len(arr) < 3:
        return False

    if arr[0] > arr[1]:           #If second value is larger than first, then it must be false.
        return False

    for i in range(1, len(arr)):
        if isIncreasing:
            if arr[i] <= arr[i-1]:  #If the current value is smaller than previous, then it has to start descending.
                isIncreasing = False
        if not isIncreasing:
            if arr[i] >= arr[i-1]:
                isMountain = False

    return isMountain

arr = [0,3,2,1]
print(validMountainArray(arr))

arr = [2,1]
print(validMountainArray(arr))

arr = [3,5,5]
print(validMountainArray(arr))

arr = [1,2,3,4,5,4,3,2,1]
print(validMountainArray(arr))


