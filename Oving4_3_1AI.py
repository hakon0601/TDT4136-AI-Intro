from random import randrange, random
from math import exp
from copy import deepcopy

#sets up first board with egges in the k first rows
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

#function to print board and score
def print_board(board_to_print):
	for y in range(m):
		print(board_to_print[y])
	print(get_score(board_to_print))

#get scores depending on conflicts
def get_score(board_to_calc):
	invalid_score = 0
	invalid_score += get_score_horizontal_and_vertical(board_to_calc)
	invalid_score += checkDiagonalsLeftTopToBotRightTopEdge(board_to_calc)
	invalid_score += checkDiagonalsLeftTopToBotRightLeftEdge(board_to_calc)
	rotated_board_to_calc = [list(a) for a in zip(*board_to_calc[::-1])]
	invalid_score += checkDiagonalsLeftTopToBotRightTopEdge(rotated_board_to_calc)
	invalid_score += checkDiagonalsLeftTopToBotRightLeftEdge(rotated_board_to_calc)
	#invalid_score += checkDiagonalsLeftBotToRightTopBotEdge(board_to_calc)
	#invalid_score += checkDiagonalsLeftBotToTopRightLeftEdge(board_to_calc)
	return maxScore - invalid_score

#get scores in vertical an horizontal direction
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

#get diagonal scores
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

#get diagonal scores
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

#get diagonal scores
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

#get diagonal scores
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

#generate different neghbours
>>>>>>> 7edba316bd2ff41ea3aecf6add2240fa8b0849e3
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
	
#pick out best neighbours
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

#starts the algorithm with getting and setting values
m = int(input("M value: "))
n = int(input("N value: "))
k = int(input("K value: "))
maxScore = 100
bestscore = min(m, n) * k
temperature = 1 # anything high?
temperature_decay = 0.001

startBoard = set_up_board()
currBoard = startBoard
best_board = startBoard
print_board(currBoard)

getListOfNeighbours(currBoard)

#general algorithm
score = get_score(currBoard)
while (score < 100 and temperature > temperature_decay):
    neighbour = getPrettyGoodNeighbour(currBoard) #this is the problem, should pick a better neighbour with higher score
    neighbourScore = get_score(neighbour)
    if (score < neighbourScore): # take temp into consideration
        currBoard = neighbour
    elif (exp(score - neighbourScore / temperature) < random()): # is true more frequently when temperature is high
        currBoard = neighbour
    temperature -= temperature_decay
    score = get_score(currBoard)

    if(get_score(best_board) < score):
        best_board = neighbour
print_board(best_board)

print_board(bestscore)

f = open('answerFile4.txt','w')
for line in bestscore:
	f.write("%s\n" % line)
f.close()
