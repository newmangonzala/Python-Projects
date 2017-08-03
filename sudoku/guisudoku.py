from random import randint
WIDTH = 81
NUM_INT = 20

class Tile():

    def __init__(self):
        self.number = False

grid = [ [Tile() for n in range(9)] for n in range(9) ]

for n in range(NUM_INT):

    while True:    
        x = randint(0,8)
        y = randint(0,8)
        if grid[y][x].number == False:
            grid[y][x].number = True
            break




def setup():
    size(800,600)

def draw(grid):
    y = 0
    for row in grid:
        x = 0
        for tile in row:
            if tile.number == True:
                fill(255,0,0)
            else:
                fill(255)
            rect(x,y,WIDTH,WIDTH)
        y +=WIDTH    
setup()
draw(grid)



