#-----------------------------------------------------------------
#   Description:    Python Coursework
#   Author:         Mark Villar                    Date: 22-11-16
#   Student ID:     UP773229
#-----------------------------------------------------------------

from graphics import *

# Circle Patch
def drawPatch(window, x, y, colour):
    radius = 10
    yCord = 90
    for i in range(10):
        circle = Circle(Point(x, y), radius)
        circle.draw(window)
        circle.setOutline(colour)
        radius = radius + 10
        yCord = yCord - 10

# Second patch shade
def shade(window, topLeftX, topLeftY, bottomRightX, bottomRightY, colour):
    rect = Rectangle(Point(topLeftX, topLeftY), Point(bottomRightX, bottomRightY))
    rect.setFill(colour)
    rect.draw(window)

def singleAntepenultimatePatch():
    window = GraphWin("Window", 100, 100)

    #Midde Red Squares
    topLeftX = 15
    topLeftY = 0
    
    bottomRightX = 25
    bottomRightY = 10
    
    for o in range(5):
        
        for i in range(4):
            shade(window, topLeftX, topLeftY, bottomRightX, bottomRightY, "red")
            #Move both X coordinates to the right
            topLeftX = topLeftX + 20
            bottomRightX = bottomRightX + 20
            
        if topLeftX > 75:
            topLeftX = 15
        if bottomRightX > 85:
            bottomRightX = 25
        
        #Move downwards
        topLeftY = topLeftY + 20
        bottomRightY = bottomRightY + 20

    #Half Red Squares (Edges)
    topLeftX = 0
    topLeftY = 0
    
    bottomRightX = 5
    bottomRightY = 10
    
    for p in range(5):
        
        for j in range(2):
            shade(window, topLeftX, topLeftY, bottomRightX, bottomRightY, "red")
            #Move all the way to the right
            topLeftX = topLeftX + 95
            bottomRightX = bottomRightX + 95
            
        if topLeftX >= 95:
            topLeftX = 0
        if bottomRightX >= 100:
            bottomRightX = 5
        
        #Move downwards
        topLeftY = topLeftY + 20
        bottomRightY = bottomRightY + 20
    
    #White Rows
    topLeftX = 0
    topLeftY = 10
    
    bottomRightX = 20
    bottomRightY = 20
    
    for z in range(5):
        
        for k in range(5):
            shade(window, topLeftX, topLeftY, bottomRightX, bottomRightY, "white")
            #Move coordinates to the right
            topLeftX = topLeftX + 20
            bottomRightX = bottomRightX + 20
        
        if topLeftX > 80:
            topLeftX = 0
        if bottomRightX > 100:
            bottomRightX = 20
        
        #Move downwards
        topLeftY = topLeftY + 20
        bottomRightY = bottomRightY + 20

def createWindow():
    while True:
        size = eval(input("Enter Window Size: "))
        
        if size == 500:
            win = GraphWin("Patches", 500, 500)
            break
        if size == 700:
            win = GraphWin("Patches", 700, 700)
            break
        if size == 900:
            win = GraphWin("Patches", 900, 900)
            break

def main():
    createWindow()

def createWindow():
    while True:
        size = eval(input("Enter Window Size: "))
        
        if size == 500:
            win = GraphWin("Patches", 500, 500)
            break
        if size == 700:
            win = GraphWin("Patches", 700, 700)
            break
        if size == 900:
            win = GraphWin("Patches", 900, 900)
            break

def main():
    createWindow()