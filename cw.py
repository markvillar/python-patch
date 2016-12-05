#-----------------------------------------------------------------
#   Description:    Python Coursework
#   Author:         Mark Villar                    Date: 22-11-16
#   Student ID:     UP773229
#-----------------------------------------------------------------
import math
from graphics import *

# Circle Patch
def circlePatch(window, xOrigin, yOrigin, colour):
    
    #Square Box
    rect = Rectangle(Point(xOrigin, yOrigin), Point(xOrigin + 100, yOrigin + 100))
    rect.draw(window)    
    
    #Circle will start small in the middle and lower part of the square
    xOrigin = xOrigin + 50
    yOrigin = yOrigin + 90
    radius = 5
    
    #Create circles
    for i in range(10):
        circle = Circle(Point(xOrigin, yOrigin), radius)
        circle.draw(window)
        circle.setOutline(colour)
        radius = radius + 5
        yOrigin = yOrigin - 5

# Penultimate patch's square drawer
def drawSquare(window, topLeftX, topLeftY, bottomRightX, bottomRightY, colour):
    rect = Rectangle(Point(topLeftX, topLeftY), Point(bottomRightX, bottomRightY))
    rect.setFill(colour)
    rect.draw(window)
    
# Penultimate Patch
def penultimatePatch(window, xOrigin, yOrigin, colour):
    
    #Inverted Background
    drawSquare(window, xOrigin, yOrigin, xOrigin + 100, yOrigin + 100, colour)
    
    #White Square top left coodinates
    whiteSquareXCoordinates = list(range(xOrigin + 5, xOrigin + 86, 20))
    whiteSquareYCoordinates = list(range(yOrigin, yOrigin + 101, 20))
    
    #White rectangular shape top left coordinates
    whiteRectangularXCoordinates = list(range(xOrigin, xOrigin + 101, 20))
    whiteRectangularYCoordinates = list(range(yOrigin + 10, yOrigin + 91, 20))
    
    #Penultimate patch master loop
    for y in range(yOrigin, yOrigin + 100, 10):
        for x in range(xOrigin, xOrigin + 100, 5):
            
            #White Squares
            if x in whiteSquareXCoordinates and y in whiteSquareYCoordinates:
                drawSquare(window, x, y, x + 10, y + 10, "white")
            
            #White Rectangles
            if x in whiteRectangularXCoordinates and y in whiteRectangularYCoordinates:
                drawSquare(window, x, y, x + 20, y + 10, "white")
            
#Gets window size from user
def getWindowSize():
    size = 0
    validSize = [5, 7, 9]
    size = eval(input("Enter Window Size: "))
    while size not in validSize:
        size = eval(input("Enter a Valid Window Size: "))
    offset = size - 1
    winSize = size * 100
    return winSize, size, offset
    
#Get 3 colours from user
def getColour():
    
    firstColour = ""
    secondColour = ""
    thirdColour = ""
    
    #Valid colours' list
    colourList = ["red", "green", "blue", "orange", "brown", "pink"]
    
    firstColour = input("Enter the first colour:")
    while firstColour not in colourList:
        firstColour = input("Please enter a valid colour:")
    
    secondColour = input("Enter the second colour:")
    while secondColour == firstColour or secondColour not in colourList:
        secondColour = input("Please enter another valid colour:")
    
    thirdColour = input("Enter the third colour:")
    while thirdColour == secondColour or thirdColour == firstColour or thirdColour not in colourList:
        thirdColour = input("Please enter another valid colour:")
    
    return firstColour, secondColour, thirdColour
    
#Round down X and Y coodinates to their nearest hundredth
def getCoordinates(xPointer, yPointer):
    xPointer = 100 * math.floor(xPointer/100.0)
    yPointer = 100 * math.floor(yPointer/100.0)
    return xPointer, yPointer

def getIndex(xOrigin, yOrigin, offset):
    #Colour index location
    topIndex = xOrigin/100
    sideIndex = yOrigin/100
    index = (sideIndex * offset) + topIndex
    return index

#Main program
def main():
    winSize, size, offset = getWindowSize()
    win = GraphWin("Window", winSize, winSize)
    
    #Get choice of colour
    colourList = []
    colourList = getColour()
    
    stepper = 100
    
    #Master Loop
    for y in range(0, winSize, 100):
        for x in range(0, winSize, 100):
            
            #Diagonal Circle Patches
            if x == y:
                circlePatch(win, x, y, colourList[0])
            
            #Horizontal Circle Patches
            if x != 0 and y == 0:
                circlePatch(win, x, y, colourList[1])
            
            #Vertical Circle Patches
            if x == (winSize - 100) and y != (winSize - 100):
                circlePatch(win, x, y, colourList[1])
            
            #Penultimate Patches
            if x != (winSize - 100) and x != y and y != 0:
                
                #Higher level Penultimate Patches
                if x >= stepper:
                    colour = colourList[1]
                
                #Lower level Penultimate Patches
                else:
                    colour = colourList[2]
                
                penultimatePatch(win, x, y, colour)
                
        stepper = stepper + 100
    
    #Colour Cycle
    index = 1
    while True:
        
        #Get coordinates
        pointer = win.getMouse()
        xPointer = pointer.getX()
        yPointer = pointer.getY()
        
        #Return Processed Coordinates
        xOrigin, yOrigin = getCoordinates(xPointer, yPointer)
        
        #Diagonal Circle Patches
        if xOrigin == yOrigin:
            circlePatch(win, xOrigin, yOrigin, colourList[index])
            
        #Horizontal Circle Patches
        if xOrigin != 0 and yOrigin == 0:
            circlePatch(win, xOrigin, yOrigin, colourList[index])
            
        #Vertical Circle Patches
        if xOrigin == (winSize - 100) and yOrigin != (winSize - 100):
            circlePatch(win, xOrigin, yOrigin, colourList[index])
        
        #Penultimate Patches
        if xOrigin != (winSize - 100) and xOrigin != yOrigin and yOrigin != 0:
            
            #Higher level Penultimate Patches
            if xOrigin >= stepper:
                colour = colourList[index]
            
            #Lower level Penultimate Patches
            else:
                colour = colourList[index]
            
            penultimatePatch(win, xOrigin, yOrigin, colour)
            
        stepper = stepper + 100
        index = index + 1
        
        if index >= 3:
            index = 0
main()