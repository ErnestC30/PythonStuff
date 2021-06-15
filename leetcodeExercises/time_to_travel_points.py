"""
On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. 
Return the minimum time in seconds to visit all the points in the order given by points.
You can move according to these rules:
In 1 second, you can either:
move vertically by one unit,
move horizontally by one unit, or
move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
You have to visit the points in the same order as they appear in the array.
You are allowed to pass through points that appear later in the order, but these do not count as visits.
"""

def minimum_time(points):
    total_time = 0
    for i in range(1, len(points)):
        d_x = points[i][0] - points[i-1][0]
        d_y = points[i][1] - points[i-1][1]

        #Moving diagonally is always the fastest, then horizontal/vertical for the remaining points
        #This means that you only need the larger magnitude between d_y and d_x

        time = max(abs(d_y), abs(d_x))          
        total_time += time                      
    
    return total_time


points = [[1,1],[3,4],[-1,0]]
print(minimum_time(points))

points2 = [[3,2],[-2,2]]
print(minimum_time(points2))

