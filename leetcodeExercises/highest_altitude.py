"""
There is a biker going on a road trip. 
The road trip consists of n + 1 points at different altitudes. 
The biker starts his trip on point 0 with altitude equal 0.
You are given an integer array gain of length n where gain[i] is the net gain in 
altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.
"""

def highest_altitude(gain):
    highest_alt = 0
    current_alt = 0

    for i in gain:
        current_alt += i
        highest_alt = max(highest_alt, current_alt)
        
    return highest_alt

gain = [-5,1,5,0,-7]
print(highest_altitude(gain))
        
gain2 = [-4,-3,-2,-1,4,3,2]
print(highest_altitude(gain2))