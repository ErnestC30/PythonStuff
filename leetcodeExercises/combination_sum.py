"""
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.
The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.
It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
"""

def combinationSum(candidates, target):
    combinations = {}                                   #Contains sum: combinations
    combinations[target] = []                           #Base case where target can be made from combinations

    for value in candidates:
        dfs(candidates, target, [value], combinations)

    return combinations[target]

 
def dfs(candidates, target, currentComb, combinations): #Depth first search method to find all combinations
    currentSum = sum(currentComb)

    if currentSum in combinations:                      #Add the current combination to the dictionary if not already in.
        currentComb.sort()
        if currentComb not in combinations[currentSum]:
            combinations[currentSum].append(currentComb)
    
    else:                                             
        combinations[currentSum] = [currentComb]        #If it is a new sum, then add it to the dictionary.
       
    if sum(currentComb) == target:
        return

    if sum(currentComb) < target:
        for value in candidates:
            dfs(candidates, target, currentComb + [value], combinations)

        
        
candidates = [2,3,6,7]
target = 7
print(combinationSum(candidates, target))

candidates = [1]
target = 2
print(combinationSum(candidates, target))

candidates = [2,3,5]
target = 8
print(combinationSum(candidates, target))

