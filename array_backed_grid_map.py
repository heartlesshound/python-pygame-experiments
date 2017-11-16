import pygame
import random

BLACK = (0, 0, 0)
BLUE = (0, 76,153)
GREEN = (102, 204, 0)
YELLOW = (255,255,0)
BROWN = (124, 85, 17)
DARK_GREEN = (36, 94, 36)
LIGHT_BLUE = (0, 128, 255)
GREY = (160, 160, 160)
WHITE = (255, 255, 255)

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


def buildArray(mapArray):

    print("In buildArray")
    for row in range(MAPHEIGHT+1):
        
        #print("row is ", row)
        #Add an empty array that will hold each cell in this row
        mapArray.append([])
        print(row)
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
                makeLand(mapArray, row, column)

                #mapArray[row].append(1)
                #print("On land", column)


def adjustMap(mapArray):

    rowLength = LANDALLOWED # = 76
    rowLength = rowLength // 2 # = 38

    minRowLength = rowLength // 2 # = 18
    
    westSea = random.randint(minRowLength, rowLength)
    eastSea = random.randint(minRowLength, rowLength)

    if westSea == eastSea:
        eastSea = random.randint(minRowLength, rowLength)
        print("Rerolled east sea") 
        

    westLand = rowLength - westSea
    eastLand = rowLength - eastSea

    totalSea = westSea + eastSea
    totalLandTiles = LANDENDE * LANDENDE

    print("totalsea = ", totalSea, "totalLandTiles = ", totalLandTiles)

    print("in adjustmap ")
    
    for i in range(LANDALLOWED):
        if i == 3:
            makeThirdRow(mapArray, westSea, westLand, eastLand, i)
            #print(mapArray[i])
        else:
            adjustLand(mapArray, westSea, i)

    paintMap(mapArray)
    

def makeThirdRow(mapArray, westSea, westLand, eastLand, i):
    print("in makethirdrow ")
    #print("WestSea = ", westSea," WestLand = ", westLand)
    #print("EastSea = ", eastSea," EastLand = ", eastLand)

    #mapArray[3][westSea] = 5
    allLand = westLand + westSea + eastLand
    #print("All Land = ", allLand)

    for column in range(3, LANDENDE):

        if column <= westSea:
            #mapArray[i][column] = []
            mapArray[i][column] = 5 
            
        elif column >= allLand:
            #mapArray[i][column] = []
            mapArray[i][column] = 5
            
        else:
            mapArray[i][column] = 1

    pass

def adjustLand(mapArray, westSea, i):
    #print("In adjust land!")
    if i >= 4:
        
        lastRow = i - 1
        
        minLandStart = (mapArray[lastRow].index(1))# finds the first instance of 1
        minLandEnd = minLandStart + mapArray[lastRow].count(1)# counts how many 1's

        landStart = random.randint(3, minLandStart)
        landEnd = random.randint(minLandEnd, LANDENDE)
        #allLand = landEnd + westSea

        for column in range(3, LANDENDE):
            if column <= landStart:
                mapArray[i][column] = 5
            elif column >= landEnd:
                mapArray[i][column] = 5
            else:
                
                mapArray[i][column] = 1
        print("in adjustlands if ")        
        #print("min land start = ", minLandStart)
        #print("min land end = ", minLandEnd)
        #print("all land = ", allLand)

    pass
    

    
def makeLand(mapArray, row, column):
    #print("In makeland")
    #isLand = random.randint(1, 4)# Selects a random tile colour
    #mapArray[row].append(isLand)
    mapArray[row].append(1)

    pass
'''
    if row == 11:
        if column == 15:
            mapArray[row].append(4)
'''

def paintMap(mapArray):
    print("in paintmap")
    for row in range(MAPHEIGHT+1):
        for column in range(MAPWIDTH+1):
            if mapArray[row][column] == 0:
                color = BLUE
            if mapArray[row][column] == 1:
                color = GREEN
            if mapArray[row][column] == 2:
                color = YELLOW
            if mapArray[row][column] == 3:
                color = BROWN
            if mapArray[row][column] == 4:
                color = DARK_GREEN
            if mapArray[row][column] == 5:
                color = LIGHT_BLUE
                
            pygame.draw.rect(screen, color,[(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    #print("end row")

def printStuff(mapArray):
    for i in range(MAPHEIGHT):
        print("Should be land",mapArray[i][4])

buildArray(mapArray)
#printStuff(mapArray)
adjustMap(mapArray)


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
