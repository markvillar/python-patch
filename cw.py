#-----------------------------------------------------------------
#   Description:    Python Coursework
#   Author:         Mark Villar                    Date: 22-11-16
#   Student ID:     UP773229
#-----------------------------------------------------------------

from graphics import *

# Circle Patch
def criclePatch(window, xStartPoint, yStartPoint, colour):
    
    xStartPoint = xStartPoint + 50
    yStartPoint = yStartPoint + 90

    radius = 5
    
    for i in range(10):
        circle = Circle(Point(xStartPoint, yStartPoint), radius)
        circle.draw(window)
        circle.setOutline(colour)
        radius = radius + 5
        yStartPoint = yStartPoint - 5

# Second Patch
def penultimatePatch(window, xStartPoint, yStartPoint, colour):

    #Midde Red Squares
    topLeftX = xStartPoint + 15
    topLeftY = yStartPoint
    
    bottomRightX = xStartPoint + 25
    bottomRightY = yStartPoint + 10
    
    for o in range(5):
        
        for i in range(4):
            shade(window, topLeftX, topLeftY, bottomRightX, bottomRightY, colour)
            #Move both X coordinates to the right
            topLeftX = topLeftX + 20
            bottomRightX = bottomRightX + 20
            
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
    
    for p in range(5):
        
        for j in range(2):
            shade(window, topLeftX, topLeftY, bottomRightX, bottomRightY, colour)
            #Move all the way to the right
            topLeftX = topLeftX + 95
            bottomRightX = bottomRightX + 95
            
        if topLeftX > (95 + xStartPoint):
            topLeftX = xStartPoint
        if bottomRightX > (100 + xStartPoint):
            bottomRightX = xStartPoint + 5
        
        #Move downwards
        topLeftY = topLeftY + 20
        bottomRightY = bottomRightY + 20
    
    #White Rows
    topLeftX = xStartPoint
    topLeftY = yStartPoint + 10
    
    bottomRightX = xStartPoint + 20
    bottomRightY = yStartPoint + 20
    
    for z in range(5):
        
        for k in range(5):
            shade(window, topLeftX, topLeftY, bottomRightX, bottomRightY, "white")
            #Move coordinates to the right
            topLeftX = topLeftX + 20
            bottomRightX = bottomRightX + 20
        
        if topLeftX > (80 + xStartPoint):
            topLeftX = xStartPoint
        if bottomRightX > (100 + xStartPoint):
            bottomRightX = xStartPoint + 20
        
        #Move downwards
        topLeftY = topLeftY + 20
        bottomRightY = bottomRightY + 20
    
    #Line on Top
    line = Line(Point(xStartPoint, yStartPoint), Point(xStartPoint + 100, yStartPoint))
    line.draw(window)

# Second patch shade
def shade(window, topLeftX, topLeftY, bottomRightX, bottomRightY, colour):
    rect = Rectangle(Point(topLeftX, topLeftY), Point(bottomRightX, bottomRightY))
    rect.setFill(colour)
    rect.draw(window)

def getWindowSize():
    size = 0
    validSize = [5, 7, 9]
    while size not in validSize:
        size = eval(input("Enter Window Size: "))
    winSize = size * 100
    return winSize, size

def main():
    winSize, size = getWindowSize()
    win = GraphWin("Window", winSize, winSize)
    
    # Temp colour
    firstColour = "brown"
    secondColour = "orange"
    thirdColour = "pink"
    
    #Number of loops dependant on winSize
    if size == 5:
        loop = 5
    elif size == 7:
        loop = 7
    elif size == 9:
        loop = 9

    # X and Y Origin
    xOrigin = 0
    yOrigin = 0

    #Diagonal circlePatch loop
    for i in range(loop):
        criclePatch(win, xOrigin, yOrigin, firstColour)
        xOrigin = xOrigin + 100
        yOrigin = yOrigin + 100
    
    #Horizontal circlePatch loop
    xOrigin = 100
    yOrigin = 0
    
    for i in range(loop - 1):
        criclePatch(win, xOrigin, yOrigin, secondColour)
        xOrigin = xOrigin + 100
    
    #Vertical circlePatch loop
    xOrigin = winSize - 100
    yOrigin = 100
    
    for i in range(loop - 2):
        criclePatch(win, xOrigin, yOrigin, secondColour)
        yOrigin = yOrigin + 100
main()