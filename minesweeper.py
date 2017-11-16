#-------------------------#
#------Minesweeper--------#
#-------------------------#

# Expert level has 24 x 24 tiles and 99 mines

import pygame
import numpy as np
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255,255,0)
BROWN = (124, 85, 17)
DARKGREEN = (36, 94, 36)
GREY = (133, 145, 162)

# Set the width and height of each grid location
WIDTH = 30
HEIGHT = 30

# Set the width of the gridlines
MARGIN = 1

xgridtile = MARGIN + WIDTH
ygridtile = MARGIN + HEIGHT

# Set the Width and Height of the map
MAPWIDTH = 10
MAPHEIGHT = 10

# Map window size
X_WIN_SIZE = ((WIDTH * (MAPWIDTH))+ (MARGIN * MAPWIDTH))
Y_WIN_SIZE = ((HEIGHT * (MAPHEIGHT))+ (MARGIN * MAPHEIGHT))
WINDOW_SIZE = ((X_WIN_SIZE), (Y_WIN_SIZE))

# Menu size
X_MENU_SIZE = 130
Y_MENU_SIZE = 310
MENU_SIZE = [(X_MENU_SIZE), (Y_MENU_SIZE)] 

# Screen size
X_SCREEN_SIZE = X_WIN_SIZE + X_MENU_SIZE
Y_SCREEN_SIZE = Y_WIN_SIZE
SCREEN_SIZE = [(X_SCREEN_SIZE), (Y_SCREEN_SIZE)]

# Button sizes
X_BTN_SIZE = 90
Y_BTN_SIZE = 40
BTN_SIZE = [(X_BTN_SIZE), (Y_BTN_SIZE)]

LIVES = 3

# Create the array
mapArray = np.zeros((MAPWIDTH, MAPHEIGHT))

# Screen  and pygame init
pygame.init()

# Set the width and height of the screen [width, height]
screen = pygame.display.set_mode(SCREEN_SIZE)

menu_surf = pygame.Surface((MENU_SIZE))
menu_surf.fill(GREY)

turns_surf = pygame.Surface((BTN_SIZE))
turns_surf.fill(WHITE)

menu_surf.blit(turns_surf, [20, 10])
screen.blit(menu_surf, [311, 0])

print("Screen size ",SCREEN_SIZE)

pygame.display.set_caption("Minesweeper")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
mine_list = []

def place_mines(mapArray):

    mines = 19
    while mines >= 0:    
        for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):

                is_a_mine = random.randint(1, 100)                

                if is_a_mine >= 75 and mines >= 0:

                    mine_list.extend([[row, column]])
                    print(mine_list)

                    mines_per_row = len(mine_list)
                    print("mines_per_row ", mines_per_row)
                    
                    mapArray[row][column] = 9
                    mines = mines - 1
                    print("mines = ", mines)

    #return (mapArray, mine_list)
                    
def check_for_mines(mine_list, LIVES):
    pos = pygame.mouse.get_pos()
    column = pos[0] // (WIDTH + MARGIN)
    row = pos[1] // (HEIGHT +MARGIN)
    tile_value = mapArray[row][column]
    print("Tile value is ", tile_value)
    print("Click ", pos, "Grid coords: ", row, column)

    if tile_value == 9:
        #print("mine list ", mine_list)
        print("You hit a mine at ", tile_value)
        color = BLACK
        LIVES = LIVES - 1

        if LIVES == 0:
            print("game over")
            
    
    else:
        color = WHITE
        nearby_mines_num = mines_nearby(mine_list, row, column, tile_value)
        print("This tile is safe ", tile_value)
        print("nearby_mines_num ", nearby_mines_num)
        #nearby_mines_num(mine_list)

    pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
    return(LIVES)

def mines_nearby(mine_list, row, column, tile_value):
 
    nearby_mines_num = 1
    return nearby_mines_num

def paint_map(mapArray):
    print("Starting row")
    
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            if mapArray[row][column] == 0:
                color = GREY
            if mapArray[row][column] == 1:
                color = GREEN
            if mapArray[row][column] == 2:
                color = YELLOW
            if mapArray[row][column] == 3:
                color = BROWN
            if mapArray[row][column] == 4:
                color = DARKGREEN

            pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
            
paint_map(mapArray)
place_mines(mapArray)
print(mapArray)

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        elif event.type == pygame.MOUSEBUTTONDOWN:
            LIVES = check_for_mines(mine_list, LIVES)
            


    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


pygame.quit()
 
#print(mapArray)
#print("Should be sea",mapArray[3][LANDENDE])
#print("Should be land",mapArray[3][LANDENDE - 1])
