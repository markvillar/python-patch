from graphics import *

def drawPatch(window, x, y, colour):
    radius = 10
    yCord = 90
    for i in range(10):
        circle = Circle(Point(x, y), radius)
        circle.draw(window)
        circle.setOutline(colour)
        radius = radius + 10
        yCord = yCord - 10

def penultimatePatch():
    win = GraphWin("Penultimate Design", 100, 100)
    
    #Five Red Patches (Rows)
    topLeftYCord = 0
    bottomRightYCord = 10
    
    for i in range(5):
        #Six Red Patches (Columns)
        topLeftXCord = -5
        bottomRightXCord = 5
        
        for j in range(6):
            redShade = Rectangle(Point(topLeftXCord, topLeftYCord), Point(bottomRightXCord, bottomRightYCord))
            redShade.setFill("red")
            redShade.draw(win)
            
            topLeftXCord = topLeftXCord + (20)
            bottomRightXCord = bottomRightXCord + (20)
        
        topLeftYCord = topLeftYCord + (20)
        bottomRightYCord = bottomRightYCord + (20)

    #White Spaces
    whiteRectTopLeftYCord = 10
    whiteBottomRightYCord = 20
    
    for l in range(5):
        #Rows
        whiteRectTopLeftXCord = 0
        whiteBottomRightXCord = 20
        
        for k in range(5):
            rect = Rectangle(Point(whiteRectTopLeftXCord, whiteRectTopLeftYCord), Point(whiteBottomRightXCord, whiteBottomRightYCord))
            rect.draw(win)
            whiteRectTopLeftXCord = whiteRectTopLeftXCord + (20)
            whiteBottomRightXCord = whiteBottomRightXCord + (20)

        whiteRectTopLeftYCord = whiteRectTopLeftYCord + (20)
        whiteBottomRightYCord = whiteBottomRightYCord + (20)

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