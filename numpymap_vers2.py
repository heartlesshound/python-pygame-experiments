"""
 Pygame base template for opening a window
 
 Sample Python/Pygame Programs
 Simpson College Computer Science
 http://programarcadegames.com/
 http://simpson.edu/computer-science/
 
 Explanation video: http://youtu.be/vRB_983kUMc
"""

import pygame
import numpy as np
import random

np.set_printoptions(threshold=np.nan)

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255,255,0)
BROWN = (124, 85, 17)
DARKGREEN = (36, 94, 36)
RED = (255, 0, 0)
PURPLE = (255, 0, 255)

# Set the width and height of each grid location
WIDTH = 10
HEIGHT = 10

# Set the width of the gridlines
MARGIN = 1

xgridtile = MARGIN + WIDTH
ygridtile = MARGIN + HEIGHT

# Set the Width and Height of the map
MAPWIDTH = 40
MAPHEIGHT = 40

last_removed = ""
land_tile_total = 5000

half_map_width = MAPWIDTH // 2 # 10
half_map_height = MAPHEIGHT // 2 # 10

x_nw_quarter_start = (MAPWIDTH // 2) -1 # 9
y_nw_quarter_start = (MAPHEIGHT // 2) -1 # 9
x_sw_quarter_start = (MAPWIDTH // 2) -1 # 9
y_sw_quarter_start = (MAPHEIGHT // 2) -1 # 9

x_ne_quarter_start = half_map_width # 10
y_ne_quarter_start = half_map_height # 10
x_se_quarter_start = half_map_width # 10
y_se_quarter_start = half_map_height # 10

# Create the array
mapArray = np.zeros((MAPWIDTH, MAPHEIGHT))

# Screen  and pygame init
pygame.init()

# Set the width and height of the screen [width, height]
X_WIN_SIZE = ((WIDTH * (MAPWIDTH))+ (MARGIN * MAPWIDTH))
Y_WIN_SIZE = ((HEIGHT * (MAPHEIGHT))+ (MARGIN * MAPHEIGHT))
WINDOW_SIZE = [(X_WIN_SIZE), (Y_WIN_SIZE)]

print("Screen size ",WINDOW_SIZE)
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("My Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

def checklinelength(x_line_length, new_x_tile):
    line_check = x_line_length - new_x_tile

    if line_check <= 0:
        pass

def checklast(current_direction, directions, last_removed):

    print("in check last")

    while current_direction == last_removed:

        print("current direction was the same")

        directions.remove(last_removed)
        current_direction = random.choice(directions)
        directions.append(last_removed)

    return(current_direction, directions)

    #else:
        
        #return(current_direction, directions)

def adjustarray(mapArray, land_tile_total, last_removed):

    print("In adjustarray")

    mapArray[x_nw_quarter_start][y_nw_quarter_start] = 1

    new_x_tile = x_nw_quarter_start # 19
    new_y_tile = y_nw_quarter_start # 19

    x_line_length = 0
    y_line_length = 0

    whilecount = 1

    directions = ["north", "south", "east", "west"]

    while land_tile_total != 0:

        
        print("---------------------")
        print("Beginning of while ", whilecount)
        print("new_x_tile = ", new_x_tile)
        print("new_y_tile = ", new_y_tile)
        print("---------------------")
        
        # Get amount of tiles between new_x_tile and MAPWIDTH
        n_line_length_range = MAPWIDTH - new_x_tile # 21
        s_line_length_range = MAPWIDTH - new_x_tile # 21
        e_line_length_range = MAPHEIGHT - new_y_tile # 21
        w_line_length_range = MAPWIDTH - new_x_tile # 21

        # get a random direction
        current_direction = random.choice(directions)
        print("current_direction = ", current_direction)

        if whilecount >= 2:
            print("running check last")
            current_direction, directions = checklast(current_direction, directions,  last_removed)
        
        if current_direction == "north":

            last_direction = "north"
            last_removed = "south"
            
            # Get a random line length
            #x_line_length = random.randint(1, n_line_length_range)
            
            x_line_length = 2

            line_length = x_line_length + new_x_tile
            
            print("Going GREEN North ", x_line_length, "tiles")
            print("new_x_tile b4 for = ", new_x_tile)
            print("new_y_tile b4 for = ", new_y_tile)
            print("line length = ", line_length)
            
            for row in range(new_x_tile, line_length+1):
                if mapArray[row][new_y_tile] == 0:
                    row = row + 1
                    line_length = line_length - 1
                else:
                    print("row = ", row)
                    mapArray[row][new_y_tile] = int(1)
                    #print("row ", row)
                
            new_x_tile = new_x_tile - x_line_length
            print("new_x_tile = ", new_x_tile)
            print("new_y_tile = ", new_y_tile)
                
        elif current_direction == "south":

            last_direction = "south"
            last_removed = "north"

            if len(directions) == 0:
                directions = "empty"

            # Get a random line length
            #x_line_length = random.randint(1, s_line_length_range)

            x_line_length = 2

            line_length = x_line_length + new_x_tile
            
            print("Going YELLOW South ", x_line_length, "tiles")
            print("new_x_tile b4 for = ", new_x_tile)
            print("new_y_tile b4 for = ", new_y_tile)
            print("line length = ", line_length)
            
            for row in range(new_x_tile +1, line_length):
                print("row = ", row)
                mapArray[row][new_x_tile] = int(2)
                #print("row ", row)
                
            new_x_tile = new_x_tile + x_line_length    
            print("new_x_tile = ", new_x_tile)
            print("new_y_tile = ", new_y_tile)


        elif current_direction == "east":

            # Get a random line length
            #y_line_length = random.randint(1, e_line_length_range)

            y_line_length = 2
            
            print("Going BROWN East ", y_line_length, "tiles")

            last_direction = "east"
            last_removed = "west"

            if len(directions) == 0:
                directions = "empty"

            line_length = y_line_length + new_y_tile
            
            print("new_x_tile b4 for = ", new_x_tile)
            print("new_y_tile b4 for = ", new_y_tile)
            print("line length = ", line_length)            
            
            for column in range(new_y_tile +1, line_length):
                print("column= ", column)
                mapArray[new_y_tile][column] = int(3)
                
            new_y_tile = new_y_tile + y_line_length
            print("new_x_tile = ", new_x_tile)
            print("new_y_tile = ", new_y_tile)
            
        elif  current_direction == "west":

            # Get a random line length
            #y_line_length = random.randint(1, w_line_length_range)
            
            y_line_length = 2
            
            print("Going RED West ", y_line_length, "tiles")

            last_direction = "west"
            last_removed = "east"
            
            if len(directions) == 0:
                directions = "empty"
            line_length = new_y_tile - y_line_length
            
            print("new_x_tile b4 for = ", new_x_tile)
            print("new_y_tile b4 for = ", new_y_tile)
            print("line length = ", line_length)
            
            for column in range(line_length, new_y_tile+1):
                print("column", column)
                mapArray[new_y_tile][column] = int(4)
                #print("column ", column)

            new_y_tile = new_y_tile - y_line_length
            print("new_x_tile = ", new_x_tile)
            print("new_y_tile = ", new_y_tile)

        else:

            return(mapArray)

        land_tile_total = land_tile_total - 500        
        whilecount = whilecount + 1

def paintMap(mapArray):
    print("Starting painting")
    
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            if mapArray[row][column] == 0:
                color = BLUE
            if mapArray[row][column] == 1:
                color = GREEN
                print("color is color ", color)
            if mapArray[row][column] == 2:
                color = YELLOW
                print("color is color ", color)
            if mapArray[row][column] == 3:
                color = BROWN
                print("color is color ", color)
            if mapArray[row][column] == 4:
                color = RED
                print("color is color ", color)
            if mapArray[row][column] == 5:
                color = BLACK
                print("color is color ", color)

            mapArray[19][19] = 5
  
            pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])



adjustarray(mapArray, land_tile_total, last_removed)
paintMap(mapArray)
#print(mapArray)

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop



    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


pygame.quit()
 
#print(mapArray)
#print("Should be sea",mapArray[3][LANDENDE])
#print("Should be land",mapArray[3][LANDENDE - 1])
