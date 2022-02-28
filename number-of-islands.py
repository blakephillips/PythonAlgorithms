# https://leetcode.com/problems/number-of-islands/
# Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        LAND = "1"
        WATER = "0"
        
        #Number of islands 
        islandCount = 0
        
        #Directions to traverse (up, down, left, right)
        directions = [
            [1,0],
            [-1,0],
            [0,1],
            [0,-1]
        ]
        
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                #If we found unexplored land
                if grid[i][j] == "1":
                    #Must be an island
                    islandCount += 1
                    
                    #Traverse via BFS
                    queue = [[i,j]]
                    grid[i][j] = "2"
                    while len(queue) != 0:
                        pos = queue.pop(0)
                        for direction in directions:
                            x, y = pos[0] + direction[0], pos[1] + direction[1]

                            #bounds
                            if x > len(grid) - 1 or x < 0: continue
                            if y > len(grid[0]) - 1 or y < 0: continue

                            #explore, set to 2 to indicate it has been explored
                            if grid[x][y] == "1":
                                grid[x][y] = "2"
                                queue.append([x,y])
        return islandCount