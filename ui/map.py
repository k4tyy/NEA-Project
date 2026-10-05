from tile import Tile

class Map:
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
        self.tiles = [[Tile() for x in range(width)] for y in range(height)] 

        # Set up boundaries at the top and bottom
        for x in range(width):
            self.tiles[x][0].top = True
            self.tiles[x][height-1].bottom = True

        # Set up boundaries for left and right
        for y in range(height):
            self.tiles[0][y].left = True
            self.tiles[width-1][y].right = True


# function to add box

# function to add line

# function to add t-bar

# function to reflect map

myMap = Map(width=8, height=8)

print(myMap.height)
print(myMap.width)

for y in range(myMap.height):
    for x in range(myMap.width):
        if myMap.tiles[x][y].top:
            print("-", end='')
        else:
            print(" ", end='')

        if myMap.tiles[x][y].bottom:
            print("+", end='')
        else:
            print(" ", end='')

    print()