# https://leetcode.com/problems/walls-and-gates/
# You are given an m x n grid rooms initialized with these three possible values.
# -1 A wall or an obstacle.
# 0 A gate.
# INF Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
# Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be filled with INF.

#Note: using bfs traversal

from typing import List

class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        
        if len(rooms) == 0: return
        
        #Different traversal directions on grid (up down left right)
        directions = [
            [-1, 0],
            [1, 0],
            [0, -1],
            [0, 1],
        ]
        
        WALL = -1
        GATE = 0
        
        #BFS queue
        queue = []
        
        #Gather our start-points (all gates)
        for i in range(len(rooms)):
            for j in range(len(rooms[i])):
                if rooms[i][j] == GATE:
                    queue.append([i,j])
        
        #BFS traverse the grid
        while len(queue) != 0:
            
            #Grab pos of source grid tile
            pos = queue.pop(0)

            #For every direction (up, down, left, right)
            for direction in directions:
                
                #Source grid tile x,y indexes
                x, y = pos
                dx, dy = direction
                
                #Compute new indexes 
                nx = x + dx
                ny = y + dy

                #Bounds check 
                if nx > len(rooms) - 1 or nx < 0: continue
                if ny > len(rooms[0]) -1 or ny < 0: continue


                #If the room isnt a wall or gate
                if rooms[nx][ny] != WALL and rooms[nx][ny] != GATE:
                    #If the distance from closest gate is bigger then the distance from our current gate we are traversing 
                    if rooms[nx][ny] > rooms[x][y] + 1:
                        #Add one to the previous rooms distance (one further away from the start-gate)
                        rooms[nx][ny] = rooms[x][y] + 1
                        #Append node for traversal
                        queue.append([nx, ny])