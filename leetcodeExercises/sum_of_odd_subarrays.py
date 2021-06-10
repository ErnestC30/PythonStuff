"""
Given an array of positive integers arr, calculate the sum of all possible odd-length subarrays.
A subarray is a contiguous subsequence of the array.
Return the sum of all odd-length subarrays of arr.
"""

def sum_of_odd_subarrays(lst):
    size = len(lst)
    t_sum = 0
    for i in range(size):
        for j in range(i, size, 2):     #Get all odd-length subarrays for each 'i' iteration
            values = lst[i:j+1]
            t_sum += sum(values)

    return t_sum

lst = [1,4,2,5,3]
lst2 = [10,11,12]
print(sum_of_odd_subarrays(lst))
