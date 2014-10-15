from random import randrange, random
from math import exp
from copy import deepcopy


class Node:
    def __init__(self, pos_x, pos_y, is_filled, in_line_with_list):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.is_filled = is_filled
        self.in_line_with_list = in_line_with_list


def set_up_initial_nodes():
    for i in range(n):
        line = []
        for j in range(m):
            if i < k:
                line.append(Node(j, i, True, []))
            else:
                line.append(Node(j, i, False, []))
        nodes.append(line)


def setUpBoard():
    board = []
    for i in range(m):
        horizontalArray = []
        for j in range(n):
            horizontalArray.append(0)
        board.append(horizontalArray)
    return board


def setInitialBoard():
    initBoard = setUpBoard()
    for i in range(m):
        for j in range(n):
            if j < k:
                initBoard[j][i] = 1
    return initBoard


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


def print_board():
    for i in range(n):
        line = []
        for j in range(m):
            if nodes[i][j].is_filled:
                line.append(1)
            else:
                line.append(0)
        print(line)
    print('\n')


def getScore(boardToCalculate):
    totScore = 0
    totScore += checkHorizontalsAndVerticals(boardToCalculate)
    totScore += checkDiagonalsLeftTopToBotRightTopEdge(boardToCalculate)
    totScore += checkDiagonalsLeftTopToBotRightLeftEdge(boardToCalculate)
    totScore += checkDiagonalsLeftBotToRightTopBotEdge(boardToCalculate)
    totScore += checkDiagonalsLeftBotToTopRightLeftEdge(boardToCalculate)
    return max_score - totScore

def get_score_new_method(board_to_calculate):
    new_score = 0
    for y in range(n):
        for x in range(m):
            if board_to_calculate[y][x].is_filled:
                new_score += abs(k-len(board_to_calculate[y][x].in_line_with_list))
    return new_score

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
        totScore += (abs(k - scoreHorizontal) + abs(k - scoreVertical))
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
            totScore += abs(k - topLeftToDownRightFromTopLine)
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
            totScore += abs(k - topLeftToDownRightFromLeftEdge)
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
            totScore += abs(k - botLeftToTopRightFromBotEdge)
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
        totScore += abs(k - botLeftToTopRightFromLeftEdge)
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
        # if (board[borderY][borderX] == 1):
        #    return False
        borderX += 1
        borderY -= 1
    return True


def pickRandomNeighbour(currentBoard):
    # copy currentboard into neighbourboard
    neighbourBoard = deepcopy(currentBoard)
    #for neigh in currentBoard:
    #    neighbourBoard.append(neigh)
    while (True):
        x = randrange(n)
        y = randrange(m)
        if (currentBoard[y][x] == 1):
            neighbourBoard[y][x] = 0
            while (True):
                x = randrange(n)
                y = randrange(m)
                if (currentBoard[y][x] == 0):
                    neighbourBoard[y][x] = 1
                    if (isBoardsEqual(currentBoard, neighbourBoard) == False):
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



def get_neighbour_new_method(conflict_node):
    neighbour_nodes = deepcopy(nodes)
    neighbour_nodes[conflict_node.pos_y][conflict_node.pos_x].is_filled = False
    while True:
        new_random_x = randrange(m)
        new_random_y = randrange(n)
        if neighbour_nodes[new_random_y][new_random_x].is_filled == False:
            neighbour_nodes[new_random_y][new_random_x].is_filled = True
            set_in_line_with_array() # this should not be called, should just update the known nodes
            return neighbour_nodes


def get_conflict_node():
    most_conflicted_node = nodes[0][0]
    for y in range(n):
        for x in range(m):
            if nodes[y][x].is_filled and len(nodes[y][x].in_line_with_list) > len(most_conflicted_node.in_line_with_list):
                most_conflicted_node = nodes[y][x]
    return most_conflicted_node



def set_in_line_with_array(): # Have to partition this to make it more generic. Should be used to update lists when creating neighbour
    for y in range(len(nodes)):
        for node1 in nodes[y]:
            node1.in_line_with_list = []
            if node1.is_filled:
                for q in range(len(nodes)):
                    for node2 in nodes[q]:
                        if node1 != node2:
                            if node2.is_filled and (node1.pos_x == node2.pos_x or node1.pos_y == node2.pos_y):
                                node1.in_line_with_list.append(node2)

                stepsback = min(node1.pos_x, node1.pos_y)
                x = node1.pos_x - stepsback
                y = node1.pos_y - stepsback
                diagonal_length = min(m - x, n - y)
                for i in range(diagonal_length):
                    if node1 != nodes[y + i][x + i] and nodes[y + i][x + i].is_filled:
                        node1.in_line_with_list.append(nodes[y + i][x + i])

                stepsback = min(node1.pos_x, n-node1.pos_y-1) # double check the -1...
                x = node1.pos_x - stepsback
                y = node1.pos_y + stepsback
                diagonal_length = min(m - x, y)
                for i in range(diagonal_length):
                    if node1 != nodes[y - i][x + i] and nodes[y - i][x + i].is_filled:
                        node1.in_line_with_list.append(nodes[y - i][x + i])



m = int(input("M value: "))  # X value
n = int(input("N value: "))  # Y value
k = int(input("K value: "))
best_score = min(m, n) * k
temperature = 3000;  # anything high?
temperature_decay = 1
max_score = 100  # ...
nodes = []
set_up_initial_nodes()
set_in_line_with_array()
#board = setInitialBoard()
# board = setRandomDots()
bestBoard = nodes
print_board()

score = get_score_new_method(nodes)  # getScore(bestBoard)

while (score < 100 and temperature > 0):  # temperature may not be 100 when the ultimate solution is found
    neighbour = get_neighbour_new_method(get_conflict_node())  #getPrettyGoodNeighbour(bestBoard, 10) #this is the problem, should pick a better neighbour with higher score
    neighbourScore = get_score_new_method(neighbour) #getScore(neighbour)
    if (score < neighbourScore):  # take temp into consideration
        nodes = neighbour
    elif (exp(score - neighbourScore / temperature) < random()):  # is true more frequently when temperature is high
        nodes = neighbour
    temperature -= temperature_decay
    score = get_score_new_method(nodes) #getScore(board)
    if get_score_new_method(bestBoard) < neighbourScore: #(getScore(bestBoard) < neighbourScore):
        bestBoard = neighbour
print_board()


