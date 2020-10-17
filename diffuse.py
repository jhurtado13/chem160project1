import random
from random import choice
npart=500
side=35  #Should be an odd number
density=random.random()
maxsteps=10000
perc=0
steps = [(1,0),(-1,0),(0,1),(0,-1)]
grid=[[0 for x in range(side)] for y in range(side)]
for i in range(len(grid)):
    for j in range(len(grid[0])):
        temp=random.random()
        if temp>density:
            grid[i][j]=1
x,y = side//2,side//2
    # perform the random walk until particle departs
for i in range(maxsteps):
    if grid[x][y]==1:
        continue
    grid[x][y]=0   #Remove particle from current spot
    sx,sy = choice(steps)
    x += sx
    y += sy
    if x<0 or y<0 or x==side or y==side:
        perc+=1
        break
    grid[x][y]=1   #Put particle in new location
print(perc/npart)
