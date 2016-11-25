#-----------------------------------------------------------------
#   Description:    Python Coursework
#   Author:         Mark Villar                    Date: 22-11-16
#   Student ID:     UP773229
#-----------------------------------------------------------------

from graphics import *

# Circle Patch
def criclePatch(window, xStartPoint, yStartPoint, colour):

    #Rectangular Box
    rect = Rectangle(Point(xStartPoint, yStartPoint), Point(xStartPoint + 100,yStartPoint + 100))
    rect.draw(window)    
    
    xStartPoint = xStartPoint + 50
    yStartPoint = yStartPoint + 90

    radius = 5
    
    for i in range(10):
        circle = Circle(Point(xStartPoint, yStartPoint), radius)
        circle.draw(window)
        circle.setOutline(colour)
        radius = radius + 5
        yStartPoint = yStartPoint - 5

# Penultimate Patch
def penultimatePatch(window, xStartPoint, yStartPoint, colour):

    #Midde Red Squares
    topLeftX = xStartPoint + 15
    topLeftY = yStartPoint
    
    bottomRightX = xStartPoint + 25
    bottomRightY = yStartPoint + 10
    
    #Fill all 5 rows
    for o in range(5):
        
        #Place 4 squares for each row
        for i in range(4):
            shade(window, topLeftX, topLeftY, bottomRightX, bottomRightY, colour)
            #Move both X coordinates to the right
            topLeftX = topLeftX + 20
            bottomRightX = bottomRightX + 20
        
        #Prevent coordinates from going beyond 100x100
        if topLeftX > (75 + xStartPoint):
            topLeftX = xStartPoint + 15
        if bottomRightX > (85 + xStartPoint):
            bottomRightX = xStartPoint + 25
        
        #Move downwards
        topLeftY = topLeftY + 20
        bottomRightY = bottomRightY + 20

    #Half Red Squares (Edges)
    topLeftX = xStartPoint
    topLeftY = yStartPoint
    
    bottomRightX = xStartPoint + 5
    bottomRightY = yStartPoint + 10
    
    #Fill all 5 rows
    for p in range(5):
        
        #Place two half squares (on start and end) for each row
        for j in range(2):
            shade(window, topLeftX, topLeftY, bottomRightX, bottomRightY, colour)
            
            #Move all the way to the right (End side)
            topLeftX = topLeftX + 95
            bottomRightX = bottomRightX + 95
        
        #Prevent coordinates from going beyond 100x100
        if topLeftX > (95 + xStartPoint):
            topLeftX = xStartPoint
        if bottomRightX > (100 + xStartPoint):
            bottomRightX = xStartPoint + 5
        
        #Move to the next row
        topLeftY = topLeftY + 20
        bottomRightY = bottomRightY + 20
    
    #White Suqares
    topLeftX = xStartPoint
    topLeftY = yStartPoint + 10
    
    bottomRightX = xStartPoint + 20
    bottomRightY = yStartPoint + 20
    
    
    for z in range(5):
        
        #Fill rows with 5 squares each
        for k in range(5):
            shade(window, topLeftX, topLeftY, bottomRightX, bottomRightY, "white")
            #Move coordinates to the right
            topLeftX = topLeftX + 20
            bottomRightX = bottomRightX + 20
        
        #Prevent coordinates from going beyond 100x100
        if topLeftX > (80 + xStartPoint):
            topLeftX = xStartPoint
        if bottomRightX > (100 + xStartPoint):
            bottomRightX = xStartPoint + 20
        
        #Move to the next row
        topLeftY = topLeftY + 20
        bottomRightY = bottomRightY + 20
    
    #Create a line on top of the patch
    line = Line(Point(xStartPoint, yStartPoint), Point(xStartPoint + 100, yStartPoint))
    line.draw(window)

# Penultimate patch square shade
def shade(window, topLeftX, topLeftY, bottomRightX, bottomRightY, colour):
    rect = Rectangle(Point(topLeftX, topLeftY), Point(bottomRightX, bottomRightY))
    rect.setFill(colour)
    rect.draw(window)

def getWindowSize():
    size = 0
    validSize = [5, 7, 9]
    size = eval(input("Enter Window Size: "))
    while size not in validSize:
        size = eval(input("Enter a Valid Window Size: "))
    winSize = size * 100
    return winSize, size

def colourValidation(firstColour, secondColour):
    
    colourList = ["red", "green", "blue", "orange", "brown", "pink"]
    
    while (secondColour == firstColour and secondColour not in colourList) or secondColour not in colourList:
        secondColour = input("Please enter another colour:")
    else:
        return secondColour

def getColour():
    firstColour = colourValidation("white", input("Enter the first colour:"))
    
    secondColour = colourValidation(firstColour, input("Enter the second colour:"))
    
    thirdColour = colourValidation(secondColour, input("Enter the third colour:"))
    
    thirdColour = colourValidation(firstColour, thirdColour)
    
    return firstColour, secondColour, thirdColour

def checkSize(size):
    if size == 5:
        loop = 5
    elif size == 7:
        loop = 7
    elif size == 9:
        loop = 9
    return loop

def main():
    winSize, size = getWindowSize()
    win = GraphWin("Window", winSize, winSize)
    
    firstColour, secondColour, thirdColour = getColour()
    
    #Number of loops dependant on winSize
    loop = checkSize(size)

    # X and Y Origins
    xOrigin = 0
    yOrigin = 0

    #Diagonal circle patch
    for i in range(loop):
        criclePatch(win, xOrigin, yOrigin, firstColour)
        xOrigin = xOrigin + 100
        yOrigin = yOrigin + 100
    
    #Horizontal circle Patches
    xOrigin = 100
    yOrigin = 0
    
    for i in range(loop - 1):
        criclePatch(win, xOrigin, yOrigin, secondColour)
        xOrigin = xOrigin + 100
    
    #Vertical circle patches
    xOrigin = winSize - 100
    yOrigin = 100
    
    for i in range(loop - 2):
        criclePatch(win, xOrigin, yOrigin, secondColour)
        yOrigin = yOrigin + 100

    #Higher level penultimate patches
    xOrigin = 200
    yOrigin = 100

    adder = 100
    sub = 3
    
    #Downward loop
    for j in range(loop - 2):
        
        #Sideward loop
        for i in range(loop - sub):
            penultimatePatch(win, xOrigin, yOrigin, secondColour)
            xOrigin = xOrigin + 100
        
        #Prevent coordinates from going beyond the window (100x100)
        if xOrigin >= winSize - 200:
            xOrigin = 200 + adder
        
        adder = adder + 100
        
        sub = sub + 1
        
        yOrigin = yOrigin + 100
    
    #Lower penultimate patches
    xOrigin = 0
    yOrigin = 100
    
    innerLoop = 1
    adder = 0
    
    for i in range(loop - 1):
        
        for j in range(innerLoop + adder):
            penultimatePatch(win, xOrigin, yOrigin, thirdColour)
            xOrigin = xOrigin + 100
        
        xOrigin = 0
        yOrigin = yOrigin + 100
        
        adder = adder + 1

main()