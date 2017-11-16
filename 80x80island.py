import pygame

BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

#Set the width and height of each grid location
WIDTH = 8
HEIGHT = 8

#Set the width of the gridlines
MARGIN = 1

#Set the Width and Height of the map
MAPWIDTH = 80
MAPHEIGHT = 80

LANDENDE = MAPWIDTH - 2
LANDALLOWED = MAPWIDTH - 4
print("LANDENDE",LANDENDE)
#Create the array

'''or row >= 8 and column >= 8'''

mapArray = []

# Initialize pygame
pygame.init()

#leftOver = WIDTH // 2
#print(leftOver)

X_WIN_SIZE = ((WIDTH * (MAPWIDTH+1))+ (MARGIN * MAPWIDTH))
# With WIDTH = 8, MAPWIDTH = 80, MARGIN = 1 leftOver = 4
# X_WIN_SIZE = 644
# 80 tiles of 8 width each
# Changing to WIDTH = 12 gives X_WIN_SIZE =
Y_WIN_SIZE = ((HEIGHT * (MAPHEIGHT+1))+ (MARGIN * MAPHEIGHT))

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [(X_WIN_SIZE), (Y_WIN_SIZE)]
#WINDOW_SIZE = [800, 800]
print("Screen size ",WINDOW_SIZE)

screen = pygame.display.set_mode(WINDOW_SIZE)

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()


# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop

    for row in range(MAPHEIGHT+1):
        #Add an empty array that will hold each cell in this row
        mapArray.append([])
        #print(row)
        for column in range(MAPWIDTH+1):
            
            if row <= 2  or column <= 2:
                #print("In T searow", row)
                mapArray[row].append(0)
                #print("In the sea", column)
            elif row >= LANDENDE or column >= LANDENDE:
                    #print(row)
                    mapArray[row].append(0)
                    #print("In the sea", column)
            else:
                mapArray[row].append(1)
                #print("On land", column)

    for row in range(MAPHEIGHT+1):
        for column in range(MAPWIDTH+1):
            color = BLUE
            if mapArray[row][column] == 1:
                color = GREEN
            pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

pygame.quit()
 
#print(mapArray)
#print("Should be sea",mapArray[3][LANDENDE])
#print("Should be land",mapArray[3][LANDENDE - 1])
