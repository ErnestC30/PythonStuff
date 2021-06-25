"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). 
n vertical lines are drawn such that the two endpoints of the line i is at (i, ai) and (i, 0). 
Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.

Example:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49 -> height[1] = 8 to height[8] = 7 gives a box of height 7 and width 7
"""

def largestContainer(heights):
    largestArea = 0

    for i in range(len(heights)):
        for j in range(len(heights)):
            width = j-i                               #Width is the index distance between the two heights.
            height = min(heights[j], heights[i])      #Height is the lower value between the two heights.

            area = width * height
            if area > largestArea:
                largestArea = area

    return largestArea

heights = [1,8,6,2,5,4,8,3,7]
print(largestContainer(heights))

heights = [4,3,2,1,4]
print(largestContainer(heights))

heights = [1,2,1]
print(largestContainer(heights))
