# Problem 15 - (09/06)
    # in a 2x2 grid, there are 6 ways you can arrange 2D's and 2R's 
    # it becomes a permutation of 40 possibilities choose 20
    
import numpy as np
    
grid = np.zeros((21, 21)) # grid has 21 gridpoints

for i in range(len(grid)):
    grid[-1, i] = 1
    grid[i, -1] = 1

for col in range(len(grid)-2, -1, -1):
    for row in range(len(grid)-2, -1, -1):
        grid[row][col]= grid[row][col+1] + grid[row+1][col]
        
print(grid[0][0])
