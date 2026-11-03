import pygame

#from ui.tile import Tile

class Map:

    ###################################################################################
    #tile class - subclass of Map
    ###################################################################################
    class Tile:
        def __init__(self, x: int, y:int, map: Map):
            self.x = x
            self.y = y
            self.myMap = map

            self.has_top = False
            self.has_bottom = False
            self.has_left = False
            self.has_right = False

            self.has_pellet = True

        #functions to return screen coordinates of tile
        def left(self) -> int:
            return self.x * self.myMap.tile_width + self.myMap.offset_x

        def right(self) -> int:
            return self.left() + self.myMap.tile_width

        def top(self) -> int:
            return self.y * self.myMap.tile_height + self.myMap.offset_y

        def bottom(self) -> int:
            return self.top() + self.myMap.tile_height


        #functions to return corners of tile
        def top_left(self) -> tuple[int, int]:
            return self.left(), self.top()

        def top_right(self) -> tuple[int, int]:
            return self.right(), self.top()

        def bottom_left(self) -> tuple[int, int]:
            return self.left(), self.bottom()

        def bottom_right(self) -> tuple[int, int]:
            return self.right(), self.bottom()

        #center of each tile
        def center(self) -> tuple[int, int]:
            return self.left() + self.myMap.tile_width / 2, self.top() + self.myMap.tile_height / 2

        #next tile functions
        def next_tile_right(self) -> Map.Tile:
            if self.x < self.myMap.width - 1:
                next_tile = self.myMap.tiles[self.x + 1][self.y]
            else:
                next_tile = self.myMap.tiles[0][self.y]

            return next_tile

        # TODO: Add next_tile_left, next_tile_up and next_tile_down
        def next_tile_left(self) -> Map.Tile:
            if self.x > 0:
                next_tile = self.myMap.tiles[self.x - 1][self.y]
            else:
                next_tile = self.myMap.tiles[self.myMap.map_width - 1][self.y]

            return next_tile

        def next_tile_up(self) -> Map.Tile:
            if self.y > 0:
                next_tile = self.myMap.tiles[self.x][self.y - 1]
                return next_tile
            else:
                return None

        def next_tile_down(self) -> Map.Tile:
            if self.y < self.myMap.map_height - 1:
                next_tile = self.myMap.tiles[self.x][self.y + 1]
                return next_tile
            else:
                return None

    ###################################################################################
    # End of Tile class
    ###################################################################################

    #create actual map       
    def __init__(self):
        self.width = 17
        self.height = 17

        #set size of tile
        self.tile_height = 30
        self.tile_width = 30

        self.tiles = [[Map.Tile(x, y, self) for y in range(self.height)] for x in range(self.width)] 

        #entire map block
        self.create_block(0,0,self.width,self.height, True)

        #create boxes in order of rows starting from top left
        #row 0
        self.create_block(8, 0, 1, 2)
        
        #row 1
        self.create_block(1, 1, 2, 1)
        self.create_block(4, 1, 3, 1)
        self.create_block(10, 1, 3, 1)
        self.create_block(14, 1, 2, 1)

        #row 3
        self.create_block(1, 3, 2, 1)
        self.create_block(4, 3, 1, 4)
        self.create_block(6, 3, 5, 1)
        self.create_block(8, 3, 1, 3)
        self.set_top_only(8, 3)
        self.create_block(12, 3, 1, 4)
        self.create_block(14, 3, 2, 1)

        #row 5
        self.create_block(0, 5, 3, 2)
        self.create_block(4, 5, 3, 1)
        self.set_left_only(4, 5)
        self.create_block(10, 5, 3, 1)
        self.create_block(14, 5, 3, 2)
        self.set_right_only(12, 5)

        #row 8       
        self.create_block(0, 8, 3, 2)
        self.create_block(4, 8, 1, 2)
        self.create_block(12, 8, 1, 2)
        self.create_block(14, 8, 3, 2)

        #row 9
        self.create_block(6, 9, 5, 1)
        self.create_block(8, 9, 1, 3)
        self.set_top_only(8, 9)

        #row 11
        self.create_block(1, 11, 2, 1)
        self.create_block(4, 11, 3, 1)
        self.create_block(10, 11, 3, 1)
        self.create_block(14, 11, 2, 1)
        self.create_block(2, 11, 1, 3)
        self.create_block(14, 11, 1, 3)
        self.set_top_and_right_only(2, 11)
        self.set_top_and_left_only(14, 11)

        #row 13
        self.create_block(0, 13, 1, 1)
        self.create_block(4, 13, 1, 3)
        self.create_block(6, 13, 5, 1)
        self.create_block(12, 13, 1, 3)
        self.create_block(16, 13, 1, 1)
        self.create_block(8, 13, 1, 3)
        self.set_top_only(8, 13)

        #row 15
        self.create_block(1, 15, 6, 1)
        self.create_block(10, 15, 6, 1)
        self.set_bottom_only(4, 15)
        self.set_bottom_only(12, 15)

        for y in range(self.height):
            for x in range(self.width):
                this_tile = self.tiles[x][y]

                if this_tile.has_right:
                    this_tile.next_tile_right().has_left = True



    #calculate map size
    def map_width(self):
        return self.width * self.tile_width

    def map_height(self):
        return self.height * self.tile_height

    #function to add box
    def create_block(self, top_left_x, top_left_y, block_width, block_height, has_pellet = False):
        for x in range(top_left_x, top_left_x + block_width):
            self.tiles[x][top_left_y].has_top = True
            self.tiles[x][top_left_y + block_height - 1].has_bottom = True

        for y in range(top_left_y, top_left_y + block_height):
            self.tiles[top_left_x][y].has_left = True
            self.tiles[top_left_x + block_width - 1][y].has_right = True

        for y in range(top_left_y, top_left_y + block_height):
            for x in range(top_left_x, top_left_x + block_width):
                self.tiles[x][y].has_pellet = has_pellet

    #functions to remove uncesessary lines
    #top line only
    def set_top_only(self, top_left_x, top_left_y):
        self.tiles[top_left_x][top_left_y].has_left = False
        self.tiles[top_left_x][top_left_y].has_right = False
        self.tiles[top_left_x][top_left_y].has_bottom = False

    #left line only
    def set_left_only(self, top_left_x, top_left_y):
        self.tiles[top_left_x][top_left_y].has_top = False
        self.tiles[top_left_x][top_left_y].has_right = False
        self.tiles[top_left_x][top_left_y].has_bottom = False

    #right line only
    def set_right_only(self, top_left_x, top_left_y):
        self.tiles[top_left_x][top_left_y].has_left = False
        self.tiles[top_left_x][top_left_y].has_top = False
        self.tiles[top_left_x][top_left_y].has_bottom = False

    #bottom line only
    def set_bottom_only(self, top_left_x, top_left_y):
        self.tiles[top_left_x][top_left_y].has_left = False
        self.tiles[top_left_x][top_left_y].has_right = False
        self.tiles[top_left_x][top_left_y].has_top = False

    #top and right line only
    def set_top_and_right_only(self, top_left_x: int, top_left_y):
        self.tiles[top_left_x][top_left_y].has_left = False
        self.tiles[top_left_x][top_left_y].has_bottom = False

    #top and left line only
    def set_top_and_left_only(self, top_left_x, top_left_y):
        self.tiles[top_left_x][top_left_y].has_right = False
        self.tiles[top_left_x][top_left_y].has_bottom = False

    #function to draw map
    def render(self, screen: pygame.Surface):
        #line set up
        line_colour = (66, 68, 129)
        pellet_colour = (66, 168, 129)
        line_width = 5

        self.offset_x = (screen.get_width() - self.map_width())/2
        self.offset_y = (screen.get_height() - self.map_height())/2

        #loops to run through each tile of the map
        for y in range(self.height):
            for x in range(self.width):
                this_tile = self.tiles[x][y]

                top_left_x = x * self.tile_width + self.offset_x
                top_left_y = y * self.tile_height + self.offset_y

                #draw top and bottom walls
                if this_tile.has_top:
                    pygame.draw.line(
                        screen, line_colour, this_tile.top_left(), this_tile.top_right(), line_width
                    )

                # TODO: Use new bottom_left and bottom_right methods
                if this_tile.has_bottom:
                    pygame.draw.line(
                        screen, line_colour,(top_left_x, top_left_y + self.tile_height),
                        (top_left_x + self.tile_width, top_left_y + self.tile_height), line_width
                    )

                #draw left and right walls  
                # TODO: Use new bottom_left method
                if this_tile.has_left:
                    pygame.draw.line(
                        screen, line_colour, this_tile.top_left(),
                        (top_left_x, top_left_y + self.tile_height), line_width
                    )

                # TODO: Use new top_right and bottom_right methods
                if this_tile.has_right:
                    pygame.draw.line(
                        screen, line_colour,(top_left_x + self.tile_width, top_left_y),
                        (top_left_x + self.tile_width, top_left_y + self.tile_height), line_width
                    )

                if this_tile.has_pellet:
                    pygame.draw.circle(screen, pellet_colour, this_tile.center(), 2)

#inital map array print
# for y in range(myMap.height):
#     for x in range(myMap.width):
#         if myMap.tiles[x][y].top:
#             print("-", end='')
#         else:
#             print(" ", end='')

#         if myMap.tiles[x][y].bottom:
#             print("+", end='')
#         else:
#             print(" ", end='')

#         #

#     print()

# for y in range(myMap.height):
#     for x in range(myMap.width):
#         if myMap.tiles[x][y].left:
#             print("(", end='')
#         else:
#             print(" ", end='')

#         if myMap.tiles[x][y].left:
#             print(")", end='')
#         else:
#             print(" ", end='')

#     print()
