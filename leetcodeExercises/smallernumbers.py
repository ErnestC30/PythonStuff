def smallerNumbers(nums):
    dct = {}
    for ind, num in enumerate(sorted(nums)):  #Enumerate makes index for each value in nums
        if num not in dct:
            dct[num] = ind                    #Stores the number of smaller values (because sorted list) less than than 'num' into 'dct'
    return [dct[num] for num in nums]

nums = [8,1,2,2,3]
print(smallerNumbers(nums))