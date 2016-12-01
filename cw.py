#-----------------------------------------------------------------
#   Description:    Python Coursework
#   Author:         Mark Villar                    Date: 22-11-16
#   Student ID:     UP773229
#-----------------------------------------------------------------

from graphics import *

# Circle Patch
def circlePatch(window, xStartPoint, yStartPoint, colour):
    
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

# Penultimate patch square shade
def drawSquare(window, topLeftX, topLeftY, bottomRightX, bottomRightY, colour):
    rect = Rectangle(Point(topLeftX, topLeftY), Point(bottomRightX, bottomRightY))
    rect.setFill(colour)
    rect.draw(window)

# Penultimate Patch
def penultimatePatch(window, xStartPoint, yStartPoint, colour):
    
    #Inverted Background
    drawSquare(window, xStartPoint, yStartPoint, xStartPoint + 100, yStartPoint + 100, colour)
    
    #White Square Coodinates
    whiteSquareXCoordinates = list(range(xStartPoint + 5, xStartPoint + 86, 20))
    whiteSquareYCoordinates = list(range(yStartPoint, yStartPoint + 101, 20))
    
    #White Rectangular Coordinates
    whiteRectangularXCoordinates = list(range(xStartPoint, xStartPoint + 101, 20))
    whiteRectangularYCoordinates = list(range(yStartPoint + 10, yStartPoint + 91, 20))
    
    #Penultimate Patch Master Loop
    for y in range(yStartPoint, yStartPoint + 100, 10):
        for x in range(xStartPoint, xStartPoint + 100, 5):
            
            #White Squares
            if x in whiteSquareXCoordinates and y in whiteSquareYCoordinates:
                drawSquare(window, x, y, x + 10, y + 10, "white")
            
            #White Rectangles
            if x in whiteRectangularXCoordinates and y in whiteRectangularYCoordinates:
                drawSquare(window, x, y, x + 20, y + 10, "white")
            
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
    
    #Get choice of colour
    firstColour, secondColour, thirdColour = getColour()
    
    #Number of loops dependant on winSize
    loop = checkSize(size)
    
    stepper = 100
    
    #Master Loop
    for y in range(0, winSize, 100):
        for x in range(0, winSize, 100):
            
            #Diagonal Circle Patches
            if x == y:
                circlePatch(win, x, y, firstColour)
            
            #Horizontal Circle Patches
            if x != 0 and y == 0:
                circlePatch(win, x, y, secondColour)
            
            #Vertical Circle Patches
            if x == (winSize - 100) and y != (winSize - 100):
                circlePatch(win, x, y, secondColour)
            
            #Penultimate Patches
            if x != (winSize - 100) and x != y and y != 0:
                
                #Higher level Penultimate Patches
                if x >= stepper:
                    colour = secondColour
                
                #Lower level Penultimate Patches
                else:
                    colour = thirdColour
                
                penultimatePatch(win, x, y, colour)
                
        stepper = stepper + 100
main()