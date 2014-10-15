from random import randrange, random
from math import exp
from copy import deepcopy

def setUpBoard():
    board = []
    for i in range(m):
        horizontalArray = []
        for j in range(n):
            horizontalArray.append(0)
        board.append(horizontalArray)
    return board


def setRandomDots():
    boardToRandomize = setUpBoard()
    dots = 0
    while (dots < bestscore):
        x = randrange(n)
        y = randrange(m)
        if (boardToRandomize[y][x] != 1):
            boardToRandomize[y][x] = 1
            dots += 1
    return boardToRandomize


def printBoard(boardToPrint):
    for i in range(m):
        print(boardToPrint[i])
    print(getScore(boardToPrint))


def getScore(boardToCalculate):
    totScore = 0
    totScore += checkHorizontalsAndVerticals(boardToCalculate)
    totScore += checkDiagonalsLeftTopToBotRightTopEdge(boardToCalculate)
    totScore += checkDiagonalsLeftTopToBotRightLeftEdge(boardToCalculate)
    totScore += checkDiagonalsLeftBotToRightTopBotEdge(boardToCalculate)
    totScore += checkDiagonalsLeftBotToTopRightLeftEdge(boardToCalculate)
    return maxScore - totScore


def checkHorizontalsAndVerticals(boardToCalculate):
    totScore = 0
    for i in range(m):
        scoreHorizontal = 0
        scoreVertical = 0
        for j in range(n):
            if (boardToCalculate[i][j] == 1):
                scoreHorizontal += 1
            if (boardToCalculate[j][i] == 1):  # not wirking when m != n
                scoreVertical += 1
        totScore += (max(scoreHorizontal - k, 0) + max(scoreVertical - k, 0))
    return totScore


def checkDiagonalsLeftTopToBotRightTopEdge(boardToCalculate):
    totScore = 0
    for i in range(n):
        topLeftToDownRightFromTopLine = 0
        if (n - i > k):
            borderX = i
            borderY = 0
            while (borderX < n and borderY < m):
                if (boardToCalculate[borderY][borderX] == 1):
                    topLeftToDownRightFromTopLine += 1
                borderX += 1
                borderY += 1
            totScore += max(topLeftToDownRightFromTopLine - k, 0)
    return totScore

def checkDiagonalsLeftTopToBotRightLeftEdge(boardToCalculate):
    totScore = 0
    for i in range(1, m):  # from 1 because (0, 0) already has been checked
        topLeftToDownRightFromLeftEdge = 0
        if (m - i > k):
            borderX = 0
            borderY = i
            while (borderX < n and borderY < m):
                if (board[borderY][borderX] == 1):
                    topLeftToDownRightFromLeftEdge += 1
                borderX += 1
                borderY += 1
            totScore += max(topLeftToDownRightFromLeftEdge - k, 0)
    return totScore

def checkDiagonalsLeftBotToRightTopBotEdge(boardToCalculate):
    totScore = 0
    for i in range(n):
        botLeftToTopRightFromBotEdge = 0
        if (n - i > k):
            borderX = i
            borderY = n - 1
            while (borderX < n and borderY < m):
                if (board[borderY][borderX] == 1):
                    botLeftToTopRightFromBotEdge += 1
                borderX += 1
                borderY -= 1
            totScore += max(botLeftToTopRightFromBotEdge - k, 0)
    return totScore

def checkDiagonalsLeftBotToTopRightLeftEdge(boardToCalculate):
    totScore = 0
    for i in range(k, m - 1):
        botLeftToTopRightFromLeftEdge = 0
        borderX = 0
        borderY = i
        while (borderX < n and borderY >= 0):
            if (board[borderY][borderX] == 1):
                botLeftToTopRightFromLeftEdge += 1
            borderX += 1
            borderY -= 1
        totScore += max(botLeftToTopRightFromLeftEdge - k, 0)
    return totScore

def isAllowed(y, x):
    return (checkHorizontal(y)
            and checkVertical(x)
            and checkDiagonalFromLeftTop(x, y)
            and checkDiagonalFromLeftBot(x, y))

def checkHorizontal(y):
    for i in range(n):
        if (board[y][i] == 1):
            return False
    return True

def checkVertical(x):
    for j in range(m):
        if (board[j][x] == 1):
            return False
    return True

def checkDiagonalFromLeftTop(x, y):
    stepsback = min(x, y)
    borderX = x - stepsback
    borderY = y - stepsback
    while (borderX < n and borderY < m):
        if (board[borderY][borderX] == 1):
            return False
        borderX += 1
        borderY += 1
    return True

def checkDiagonalFromLeftBot(x, y):
    stepsback = min(x, m - y)
    borderX = x - stepsback
    borderY = y - stepsback
    while (borderX < n and borderY > 0):
        if (board[borderY][borderX] == 1):
            return False
        borderX += 1
        borderY -= 1
    return True


def pickRandomNeighbour(currentBoard):
    #copy currentboard into neighbourboard
    neighbourBoard = deepcopy(currentBoard)
    #for neigh in currentBoard:
    #    neighbourBoard.append(neigh)
    while(True):
        x = randrange(n)
        y = randrange(m)
        if (currentBoard[y][x] == 1 and not isAllowed(y, x)):
            neighbourBoard[y][x] = 0
            while(True):
                x = randrange(n)
                y = randrange(m)
                if (currentBoard[y][x] == 0):
                    neighbourBoard[y][x] = 1
                    if(isBoardsEqual(currentBoard, neighbourBoard) == False):
                        return neighbourBoard

def getPrettyGoodNeighbour(currentBoard, nrOfNeighbors):
    neighbours = []
    while (len(neighbours) < nrOfNeighbors):
        neighbourBoard = pickRandomNeighbour(currentBoard)
        if (isNeighbourInNeighbourList(neighbours, neighbourBoard) == False):
            neighbours.append(neighbourBoard)

    bestNeighbour = neighbours[0]
    for i in range(1, len(neighbours)):
        if (getScore(bestNeighbour) < getScore(neighbours[i])):
            bestNeighbour = neighbours[i]
    return bestNeighbour

def isNeighbourInNeighbourList(neighbours, neighbourBoard):
    for i in range(len(neighbours)):
        if (isBoardsEqual(neighbours[i], neighbourBoard)):
            return True
    return False

def isBoardsEqual(board1, board2):
    for j in range(m):
        for k in range(n):
            if (board1[j][k] != board2[j][k]):
                return False
    return True



m = int(input("M value: "))
n = int(input("N value: "))
k = int(input("K value: "))
bestscore = min(m, n) * k
temperature = 3000 # anything high?
temperature_decay = 1
maxScore = 100  # ...
bestBoard = setRandomDots()

#printBoard(board)

score = getScore(board)
while (score < 100 and temperature > 0): # temperature may not be 100 when the ultimate solution is found
    neighbour = getPrettyGoodNeighbour(bestBoard, 10) #this is the problem, should pick a better neighbour with higher score
    neighbourScore = getScore(neighbour)
    if (score < neighbourScore): # take temp into consideration
        board = neighbour
    elif (exp(score - neighbourScore / temperature) < random()): # is true more frequently when temperature is high
        board = neighbour
    temperature -= temperature_decay
    score = getScore(board)
    if(getScore(bestBoard) < neighbourScore):
        bestBoard = neighbour
printBoard(bestBoard)