from random import randrange


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
	while(dots < bestscore):
		x =	randrange(n)
		y = randrange(m)
		if (boardToRandomize[y][x] != 1):
			boardToRandomize[y][x] = 1
			dots += 1
	return boardToRandomize

def printBoard(boardToPrint):
	for i in range(m):
		print(boardToPrint[i])
	#print(getScore(boardToPrint))

def getScore(boardToCalculate):
	totScore = 0
	#checks horizontals and verticals
	for i in range(m):
		scoreHorizontal = 0
		scoreVertical = 0
		for j in range(n):
			if (boardToCalculate[i][j] == 1):
				scoreHorizontal += 1
			if (boardToCalculate[j][i] == 1): # not wirking when m != n
				scoreVertical += 1
		totScore += (abs(k-scoreHorizontal) + abs(k-scoreVertical))
	# check diagonals leftTopToBotRight top edge
	totScore = 0
	for i in range(n):
		topLeftToDownRightFromTopLine = 0
		if (i < n-k):
			borderX = i
			borderY = 0
			while (borderX < n and borderY < m):
				if (board[borderY][borderX] == 1):
					topLeftToDownRightFromTopLine += 1
				borderX += 1
				borderY += 1

			totScore += abs(k - topLeftToDownRightFromTopLine)
	print("totScore topLeftToDownRightFromTopLine: " + str(totScore))
	# check diagonals leftTopToBotRight left edge
	for i in range(1, m): #from 1 because (0, 0) already has been checked
		topLeftToDownRightFromLeftEdge = 0
		if (i < m-k):
			borderX = 0
			borderY = i
			while (borderX < n and borderY < m):
				if (board[borderY][borderX] == 1):
					topLeftToDownRightFromLeftEdge += 1
				borderX += 1
				borderY += 1
			totScore += abs(k - topLeftToDownRightFromLeftEdge)
	# check diagonals leftBot bot edge
	for i in range(n):
		botLeftToTopRightFromBotEdge = 0
		if (i < n-k):
			borderX = i
			borderY = n - 1
			while (borderX < n and borderY < m):
				if (board[borderY][borderX] == 1):
					botLeftToTopRightFromBotEdge += 1
				borderX += 1
				borderY -= 1
			totScore += abs(k - botLeftToTopRightFromBotEdge)
	# check diagonals leftBotToTopRight left edge
	for i in range(m - 1):
		botLeftToTopRightFromLeftEdge = 0
		if (i >= k):
			borderX = 0
			borderY = i
			while (borderX < n and borderY < m):
				if (board[borderY][borderX] == 1):
					botLeftToTopRightFromLeftEdge += 1
				borderX += 1
				borderY -= 1
			totScore += abs(k - botLeftToTopRightFromLeftEdge)

	return maxScore - totScore

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
def	checkDiagonalFromLeftTop(x, y):
	stepsback = min(x, y)
	borderX = x - stepsback
	borderY = y - stepsback
	while (borderX < n and borderY < m):
		if (board[borderY][borderX] == 1):
			return False
		borderX += 1
		borderY += 1
	return True


def	checkDiagonalFromLeftBot(x, y):
	stepsback = min(x, m - y)
	borderX = x - stepsback
	borderY = y - stepsback
	while (borderX < n and borderY > 0):
		if (board[borderY][borderX] == 1):
			return False
		borderX += 1
		borderY -= 1
	return True

def pickRandomNeighbour():
	neighbours = []
	prevBoard = board
	#iterate through every egg in the carton
	for i in range(score):
		# finds all the eggs
		for j in range(m):
			for k in range(n):
				# when finding an egg, remove it and iterate through prevBoard
				if (prevBoard[j][k] == 1):
					prevBoard[j][k] = 0
					# iterates through prevBoard to find new places to place the egg
					for q in range(m):
						for r in range(n):
							if (isAllowed(q, r) and not (q == j and r == k)):
								newNeighbour = prevBoard
								newNeighbour[q][r] = 1
								neighbours.append(newNeighbour)
	print("nr of neighbours: " + str(len(neighbours)))
	return neighbours[randrange(len(prevBoard))]





#iterations = int(input("Nr of iterations: "))
m = int(input("M value: "))
n = int(input("N value: "))
k = int(input("K value: "))
bestscore = min(m, n) * k
initTemp = 300; # anything high?
maxScore = 100 # ...
board = setUpBoard()
board = setRandomDots()
bestBoard = board
printBoard(board)

score = getScore(board)

#for i in range(iterations):
#	if (score >= min(m, n)):
#	break

#neighbour = pickRandomNeighbour()
#printBoard(neighbour)


