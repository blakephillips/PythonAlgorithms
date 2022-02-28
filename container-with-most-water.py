# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.
# Notice that you may not slant the container.
from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        left = 0
        right = len(height) -1
        
        leftHighest = 0
        rightHighest = len(height) -1
        
        highestWaterStored = 0
        
        while left < right:
            
            length = right - left
            currentHeight = min(height[left], height[right])
            waterStored = length * currentHeight
            
            if waterStored > highestWaterStored: highestWaterStored = waterStored
            
            
            if height[left] > height[right]:
                right -=1
            else:
                left +=1
            
        return highestWaterStored