"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. 
Return the answer in any order.
A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.
Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
"""

def phoneCombinations(digits):
    phone_digits = {
        '2': 'abc',
        '3': 'def',
        '4': 'ghi',
        '5': 'jkl',
        '6': 'mno',
        '7': 'pqrs',
        '8': 'tuv',
        '9': 'wxyz'
    }
    if digits == '':
        return []

    total_combinations = ['']
    for digit in digits:                                            #Each letter for the current digit is appended to 
        current_combination = []                                    #every possible combination obtained from the the
        for letter in phone_digits[digit]:                          #previous digit. The total_combinations is then updated.
            for combination in total_combinations:
                current_combination.append(combination + letter)       
        total_combinations = current_combination
    return total_combinations

digits = "239"
print(phoneCombinations(digits))