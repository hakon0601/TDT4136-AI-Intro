
"""
H (Heuristic) = Distance to goal (through walls)
G (Movement Cost) = Value of movement. 1 in the first task
F = G + H
"""
import math

class Node:
	def __init__(self, pos, h, g, wall, endPos, parent):
		self.pos = pos
		self.h = h
		self.g = g
		self.wall = wall
		self.endPos = endPos
		self.parent = parent

def getPosOf(element):
	for y in range(len(board)):
		for x in range(len(board[y])):
			if (board[y][x] == element):
				return (x, y)

def printBoard():
	for line in board:
		print(line)

def printHs():
	for y in range(len(board)):
		horizontalHs = []
		for x in range(len(board[y])):
			horizontalHs.append(node2dList[y][x].h)
		print(horizontalHs)

def setupBoard(fname):
	with open(fname) as f:
		board = f.read().splitlines()
	return(board)

def getManhattanH(x, y):
	return abs(endPos[0] - x) + abs(endPos[1] - y)

#def getEuclidianH(x, y):
	#TODO easy later

def createInitialNodes():
	verticalNodeList = [] 
	for y in range(len(board)):
		horizontalNodeList = [] 		
		for x in range(len(board[y])):
			h = getManhattanH(x, y)
			g = 10000 # TODO fix
			parent = None
			if (board[y][x] == "." or board[y][x] == "A"):
				wall = False
				endPos = False
			elif (board[y][x] == "#"):
				wall = True
				endPos = False
			else:
				wall = False
				endPos = True
			horizontalNodeList.append(Node((x, y), h, g, wall, endPos, parent))
		verticalNodeList.append(horizontalNodeList)
	return verticalNodeList	


def setupChildrenOfNode(parentNode):
	if parentNode.pos[0] != 0: 
		westNode = node2dList[parentNode.pos[1]][parentNode.pos[0] - 1]
		reCheckNode(westNode, parentNode)
		if (westNode.endPos):
			return westNode

	if parentNode.pos[1] != 0:
		northNode = node2dList[parentNode.pos[1] - 1][parentNode.pos[0]]
		reCheckNode(northNode, parentNode)
		if (northNode.endPos):
			return northNode

	if parentNode.pos[1] < (len(node2dList) - 1):
		southNode = node2dList[parentNode.pos[1] + 1][parentNode.pos[0]]
		reCheckNode(southNode, parentNode)
		if (southNode.endPos):
			return southNode

	if parentNode.pos[0] < (len(node2dList[parentNode.pos[1]]) - 1):
		eastNode = node2dList[parentNode.pos[1]][parentNode.pos[0] + 1]
		reCheckNode(eastNode, parentNode)
		if (eastNode.endPos):
			return (eastNode)
	return None

def reCheckNode(node, parentNode):
	if (node.wall == False and (node not in closedList and node not in openList)): 
			if ((parentNode.g + 1) < node.g):
				node.parent = parentNode
				node.g = 1 + parentNode.g
			openList.append(node)

def getBestNodeInOpenList():
	bestNode = openList[0]
	for node in openList:
		if (node.g) < (bestNode.g):
			bestNode = node
	return bestNode

def printLists():
	oListPos = []
	for pos in openList:
		oListPos.append(pos.pos)
	print(oListPos)
	cListPos = []
	for poss in closedList:
		cListPos.append(poss.pos)
	print(cListPos)


fname = 'board-1-1.txt'
board = setupBoard(fname) # (y, x)
startPos = getPosOf("A") # (x, y)
endPos = getPosOf("B") # (x, y)
node2dList = createInitialNodes() # (y, x)...
startNode = node2dList[startPos[1]][startPos[0]]
startNode.g = 0

printBoard()

closedList = []
openList = []

openList.append(startNode) #Adding the startnode to the closed list

#printLists()
endNode = None

while(True):
	bestNode = getBestNodeInOpenList()
	openList.remove(bestNode)
	closedList.append(bestNode)
	endNode = setupChildrenOfNode(bestNode)
	if (endNode != None):
		break

print("\n")

# Altering and printing board. Comma represents the path
node = endNode
while (node.parent != None):
	s = list(board[node.pos[1]])
	s[node.pos[0]] = ","
	board[node.pos[1]] = "".join(s)
	node = node.parent

s = list(board[endPos[1]])
s[endPos[0]] = "B"
board[endPos[1]] = "".join(s)

printBoard()


f = open('answerFile.txt','w')
for line in board:
	f.write(line + '\n')
f.close()


