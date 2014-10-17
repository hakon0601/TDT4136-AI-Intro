from random import randrange, random
from math import exp
from copy import deepcopy

def set_up_board():
	board = []
	for y in range(n):
		horizontalArray = []
		for x in range(m):
			if y < k :
				horizontalArray.append(1)
			else:
				horizontalArray.append(0)
		board.append(horizontalArray)
	return board

def print_board(board_to_print):
	for y in range(m):
		print(board_to_print[y])
	print(get_score(board_to_print))

def get_score(board_to_calc):
	invalid_score = 0
	invalid_score += get_score_horizontal_and_vertical(board_to_calc)
	invalid_score += checkDiagonalsLeftTopToBotRightTopEdge(board_to_calc)
	invalid_score += checkDiagonalsLeftTopToBotRightLeftEdge(board_to_calc)
	invalid_score += checkDiagonalsLeftBotToRightTopBotEdge(board_to_calc)
	invalid_score += checkDiagonalsLeftBotToTopRightLeftEdge(board_to_calc)
	return maxScore - invalid_score


def get_score_horizontal_and_vertical(boardToCalculate):
	invalid_score = 0
	for i in range(m):
		scoreHorizontal = 0
		scoreVertical = 0
		for j in range(n):
			if (boardToCalculate[i][j] == 1):
				scoreHorizontal += 1
			if (boardToCalculate[j][i] == 1):  # not working when m != n
				scoreVertical += 1
		invalid_score += (max(scoreHorizontal - k, 0) + max(scoreVertical - k, 0))
	return invalid_score


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
				if (currBoard[borderY][borderX] == 1):
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
				if (currBoard[borderY][borderX] == 1):
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
			if (currBoard[borderY][borderX] == 1):
				botLeftToTopRightFromLeftEdge += 1
			borderX += 1
			borderY -= 1
		totScore += max(botLeftToTopRightFromLeftEdge - k, 0)
	return totScore

def getListOfNeighbours(currBoard):
	listOfNeighbours = []
	for x in range(m):
		newNeighbour = deepcopy(currBoard)
		for y in range(n):
			newNeighbour[y][x] = 0
		placedEggs = 0
		while placedEggs < k:
			randy = randrange(n)
			if newNeighbour[randy][x] == 0:
				newNeighbour[randy][x] = 1
				placedEggs += 1
		listOfNeighbours.append(newNeighbour)
	return listOfNeighbours
	


def getPrettyGoodNeighbour(currBoard):
	listOfNeighbours = getListOfNeighbours(currBoard)
	listOfBestNeighbours = []
	listOfBestNeighbours.append(listOfNeighbours[0])
	for i in range(1, len(listOfNeighbours)):
		if get_score(listOfNeighbours[i]) > get_score(listOfBestNeighbours[0]):
			listOfBestNeighbours = []
			listOfBestNeighbours.append(listOfNeighbours[i])
		elif get_score(listOfNeighbours[i]) == get_score(listOfBestNeighbours[0]):
			listOfBestNeighbours.append(listOfNeighbours[i])
	newBoard = listOfBestNeighbours[randrange(len(listOfBestNeighbours))]
	return newBoard


m = int(input("M value: "))
n = int(input("N value: "))
k = int(input("K value: "))
maxScore = 100
bestscore = min(m, n) * k
temperature = 3000 # anything high?
temperature_decay = 1

startBoard = set_up_board()
currBoard = startBoard
print_board(currBoard)

getListOfNeighbours(currBoard)

score = get_score(currBoard)
while (score < 100 and temperature > 0):
    neighbour = getPrettyGoodNeighbour(currBoard) #this is the problem, should pick a better neighbour with higher score
    neighbourScore = get_score(neighbour)
    if (score < neighbourScore): # take temp into consideration
        currBoard = neighbour
    elif (exp(score - neighbourScore / temperature) < random()): # is true more frequently when temperature is high
        currBoard = neighbour
    temperature -= temperature_decay
    score = get_score(currBoard)
    if(get_score(currBoard) < neighbourScore):
        currBoard = neighbour
print_board(currBoard)
