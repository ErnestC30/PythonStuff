def shuffleString(s, indices):
    new_str = [''] * len(s)             #Generate list of empty strings
    for ind, char in enumerate(s):
        new_str[indices[ind]] = char

    return ''.join(new_str)
        
s = "codeleet" 
indices = [4,5,6,7,0,2,1,3]    

print(shuffleString(s, indices))