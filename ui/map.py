import pygame

from ui.tile import Tile


# function to add t-bar

# function to reflect map

class Map:
    def tile_width(self):
        return 30
    
    def tile_height(self):
        return 30
           
    def __init__(self, width, height):
        self.width = int(width)
        self.height = int(height)
        self.tiles = [[Tile() for y in range(height)] for x in range(width)] 

        #entire map block
        self.create_block(0,0,width,height)

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
        self.create_block(12, 3, 1, 4)
        self.create_block(14, 3, 2, 1)
        #row 5
        self.create_block(0, 5, 3, 2)
        self.create_block(4, 5, 3, 1)
        self.create_block(10, 5, 3, 1)
        self.create_block(14, 5, 3, 2)

        #row 8       
        self.create_block(0, 8, 3, 2)
        self.create_block(4, 8, 1, 2)
        self.create_block(12, 8, 1, 2)
        self.create_block(14, 8, 3, 2)
        #row 9
        self.create_block(6, 9, 5, 1)
        #row 10
        self.create_block(8, 10, 1, 2)

        #row 11
        self.create_block(1, 11, 2, 1)
        self.create_block(4, 11, 3, 1)
        self.create_block(10, 11, 3, 1)
        self.create_block(14, 11, 2, 1)
        #row 12
        self.create_block(2, 12, 1, 2)
        self.create_block(14, 12, 1, 2)
        #row 13
        self.create_block(0, 13, 1, 1)
        self.create_block(4, 13, 1, 2)
        self.create_block(6, 13, 5, 1)
        self.create_block(12, 13, 1, 2)
        self.create_block(16, 13, 1, 1)
        #row 14
        self.create_block(8, 14, 1, 2)
        #row 15
        self.create_block(1, 15, 6, 1)
        self.create_block(10, 15, 6, 1)

    def map_width(self):
        return self.width * self.tile_width()

    def map_height(self):
        return self.height * self.tile_height()

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
    def render(self, screen: pygame.Surface):
        #line set up
        line_colour = (66, 68, 129)
        line_width = 5
        offset_x = (screen.get_width() - self.map_width())/2
        offset_y = (screen.get_height() - self.map_height())/2

        for y in range(self.height):
            for x in range(self.width):
                top_left_x = x * self.tile_width() + offset_x
                top_left_y = y * self.tile_height() + offset_y

                #draw top and bottom walls
                if self.tiles[x][y].top:
                    pygame.draw.line(
                        screen, line_colour,(top_left_x, top_left_y), (top_left_x + self.tile_width(), top_left_y), line_width
                    )

                if self.tiles[x][y].bottom:
                    pygame.draw.line(
                        screen, line_colour,(top_left_x, top_left_y + self.tile_height()), (top_left_x + self.tile_width(), top_left_y + self.tile_height()), line_width
                    )

                #draw left and right walls  
                if self.tiles[x][y].left:
                    pygame.draw.line(
                        screen, line_colour,(top_left_x, top_left_y), (top_left_x, top_left_y + self.tile_height()), line_width
                    )

                if self.tiles[x][y].right:
                    pygame.draw.line(
                        screen, line_colour,(top_left_x + self.tile_width(), top_left_y), (top_left_x + self.tile_width(), top_left_y + self.tile_height()), line_width
                    )


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

# def draw(self, screen):
#     line_colour = (66, 68, 129)
#     line_width = 5

#     if self.top:
#         pygame.draw.line(
#             screen, line_colour,(self.top_left_x, self.top_right_y), (self.top_left_x + block_width, self.top_left_y + block_height), line_width
#         )
    
