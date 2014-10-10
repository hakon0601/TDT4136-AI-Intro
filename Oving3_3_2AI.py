__author__ = "hakon0601"


class Car():
    def __init__(self, firstXPos, firstYPos, horizontal, isTrailer, isYourCar):
        self.firstX = firstXPos
        self.firstY = firstYPos
        self.horizontal = horizontal
        self.isTrailer = isTrailer
        self.isYourCar = isYourCar

def createEmptyBoard(x, y):
    for i in range(y):
        line = []
        for j in range(x):
            line.append('.')
        board.append(line)

def printBoard():
    for y in range(len(board)):
        line = ""
        for x in range(len(board[y])):
            line += board[y][x]
        print(line)

def addCar(firstXPos, firstYPos, horizontal, isTrailer):
    if (horizontal):
        board[firstYPos][firstXPos] = '#'
        board[firstYPos][firstXPos + 1] = '#'
        if (isTrailer):
            board[firstYPos][firstXPos + 2] = '#'
    else:
        board[firstYPos][firstXPos] = '$'
        board[firstYPos + 1][firstXPos] = '$'
        if (isTrailer):
            board[firstYPos + 2][firstXPos] = '$'
    cars.append(Car(firstXPos, firstYPos, horizontal, isTrailer, False))

def setYourCar(index):
    cars[index].isYourCar = True

def getYourCar():
    for car in cars:
        if (car.isYourCar):
            return car

def isRoadClear():
    car = getYourCar()
    a = "sfs"

    for i in board[car.]




board = []
cars = []
exit = (5, 2)
createEmptyBoard(6, 4)

addCar(2, 0, True, False)
addCar(3, 1, False, False)
addCar(1, 2, True, False)
addCar(0, 3, True, True)
addCar(4, 3, True, False)
setYourCar(2)


printBoard()