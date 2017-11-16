import pygame
import numpy as np

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
YELLOW = (255,255,0)
BROWN = (124, 85, 17)
DARKGREEN = (36, 94, 36)

# Set the width and height of each grid location
WIDTH = 10
HEIGHT = 10

# Set the width of the gridlines
MARGIN = 1

xgridtile = MARGIN + WIDTH
ygridtile = MARGIN + HEIGHT

# Set the Width and Height of the map
MAPWIDTH = 20
MAPHEIGHT = 20

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

directions = ["north", "east", "south", "east", "north", "north", "west", "west", "south"]

def choose_direction(directions):
    directions_len = int(len(directions))
    print("directions len = ", directions_len)
    for i in range(directions_len):
        current_direction = directions[i]
        print("current direction = ", current_direction)
        #return (current_direction)

def paint_map(mapArray):
    print("Starting row")
    
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            if mapArray[row][column] == 0:
                color = BLUE
            if mapArray[row][column] == 1:
                color = GREEN
                #print(mapArray[row][column])
                #print(color)
            if mapArray[row][column] == 2:
                color = YELLOW
            if mapArray[row][column] == 3:
                color = BROWN
            if mapArray[row][column] == 4:
                color = DARKGREEN


            xpos = column + MARGIN
            xsquare = xgridtile * xpos
            ypos = row + MARGIN
            ysquare = ygridtile * ypos

            pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
            
choose_direction(directions)
paint_map(mapArray)

# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

        elif event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT +MARGIN)
            print("Click ", pos, "Grid coords: ", row, column)


    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()


pygame.quit()
 
#print(mapArray)
#print("Should be sea",mapArray[3][LANDENDE])
#print("Should be land",mapArray[3][LANDENDE - 1])
