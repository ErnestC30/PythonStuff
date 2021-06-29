"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
"""

def generateParantheses(n):
    open, close, combinations = n, n, []                    #track number of open and close brackets uses REMAINING.
    dfs(open, close, combinations, "")                      #combination holds all possible correct parantheses combination.
    return combinations

def dfs(open, close, combinations, string):                 #use of depth first search to find all combinations.
    if close < open:                                        #can never have more open brackets available than closed ones.
        return                                              #incorrect strings are removed.

    if not open and not close:                              #when out of both bracket types, then append the finished string to combinations.
        combinations.append(string)
        return

    if open:                                                #two recursive statements, one adds open bracket the other adds a close
        dfs(open - 1, close, combinations, string + "(")

    if close:
        dfs(open, close - 1, combinations, string + ")")

n = 3
print(generateParantheses(n))