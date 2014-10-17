

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
	rotated_board_to_calc = [list(a) for a in zip(*board_to_calc[::-1])]
	invalid_score += checkDiagonalsLeftTopToBotRightTopEdge(rotated_board_to_calc)
	invalid_score += checkDiagonalsLeftTopToBotRightLeftEdge(rotated_board_to_calc)
	#invalid_score += checkDiagonalsLeftBotToRightTopBotEdge(board_to_calc)
	#invalid_score += checkDiagonalsLeftBotToTopRightLeftEdge(board_to_calc)
	return maxScore - invalid_score


def get_score_horizontal_and_vertical(boardToCalculate):
	invalid_score = 0
	for i in range(m):
		scoreHorizontal = 0
		scoreVertical = 0
		for j in range(n):
			if (boardToCalculate[i][j] == 1):
				scoreHorizontal += 1
			if (boardToCalculate[j][i] == 1):  # not wirking when m != n
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



m = int(input("M value: "))
n = int(input("N value: "))
k = int(input("K value: "))
maxScore = 100
bestscore = min(m, n) * k
temperature = 3000 # anything high?
temperature_decay = 1

board = set_up_board()
print_board(board)

score = get_score(board)
while (score < 100 and temperature > 0):
    neighbour = getPrettyGoodNeighbour(bestBoard, 10) #this is the problem, should pick a better neighbour with higher score
    neighbourScore = get_score(neighbour)
    if (score < neighbourScore): # take temp into consideration
        board = neighbour
    elif (exp(score - neighbourScore / temperature) < random()): # is true more frequently when temperature is high
        board = neighbour
    temperature -= temperature_decay
    score = getScore(board)
    if(getScore(bestBoard) < neighbourScore):
        bestBoard = neighbour
printBoard(bestBoard)