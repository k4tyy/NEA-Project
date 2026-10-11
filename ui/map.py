from tile import Tile


# function to add t-bar

# function to reflect map

class Map:
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
        self.tiles = [[Tile() for y in range(height)] for x in range(width)] 

        #entire map block
        self.create_block(0,0,width,height)

        #rows

        self.create_block(8, 0, 1, 2)

        self.create_block(1, 1, 2, 1)
        self.create_block(4, 1, 3, 1)
        self.create_block(10, 1, 3, 1)
        self.create_block(14, 1, 2, 1)

        self.create_block(1, 3, 2, 1)
        self.create_block(4, 3, 1, 5)
        self.create_block(6, 3, 5, 1)
        self.create_block(8, 3, 1, 3)
        self.create_block(12, 3, 1, 5)
        self.create_block(14, 3, 2, 1)


        self.create_block(0, 5, 3, 2)
        self.create_block(4, 5, 3, 1)
        self.create_block(12, 5, 3, 1)
        self.create_block(14, 5, 3, 2)

        #dodgy reflection
        
        self.create_block(4, 8, 1, 5)
        self.create_block(12, 8, 1, 5)

        self.create_block(0, 9, 3, 2)
        self.create_block(14, 9, 3, 2)

        self.create_block(4, 10, 3, 1)
        self.create_block(8, 10, 1, 3)
        self.create_block(12, 10, 3, 1)

        self.create_block(1, 12, 2, 1)
        self.create_block(6, 12, 5, 1)
        self.create_block(14, 12, 2, 1)

        self.create_block(1, 14, 2, 1)
        self.create_block(4, 14, 3, 1)
        self.create_block(10, 14, 3, 1)
        self.create_block(14, 14, 2, 1)

        self.create_block(8, 15, 1, 2)
    

    #function to add box
    def create_block(self, top_left_x, top_left_y, block_width, block_height):
        for x in range(top_left_x, top_left_x + block_width):
            self.tiles[x][top_left_y].top = True
            self.tiles[x][top_left_y + block_height - 1].bottom = True

        for y in range(top_left_y, top_left_y + block_height):
            self.tiles[top_left_x][y].left = True
            self.tiles[top_left_x + block_width - 1][y].right = True

    # function to add line
    # def create_horizontal_line(self, top_left_x, top_left_y):
    #     self.tiles[top_left_x][top_left_y].top = True
    #     self.tiles[top_left_x][top_left_y].bottom = True

    # def create_vertical_line(self, top_left_x, top_left_y):
    #     self.tiles[top_left_x][top_left_y].left = True
    #     self.tiles[top_left_x][top_left_y].right = True


    #    create_block(self, 1, 1, 4)

myMap = Map(width=17, height=17)

# print(myMap.height)
# print(myMap.width)

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

        #

    print()

for y in range(myMap.height):
    for x in range(myMap.width):
        if myMap.tiles[x][y].left:
            print("(", end='')
        else:
            print(" ", end='')

        if myMap.tiles[x][y].left:
            print(")", end='')
        else:
            print(" ", end='')

    print()