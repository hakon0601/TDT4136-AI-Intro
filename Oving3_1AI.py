
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

#This function gets position of given element(start/stop)
def getPosOf(element):
	for y in range(len(board)):
		for x in range(len(board[y])):
			if (board[y][x] == element):
				return (x, y)

#This prints the board at a given time
def printBoard():
	for line in board:
		print(line)

#This prints all the H-values. Help function, not used.
def printHs():
	for y in range(len(board)):
		horizontalHs = []
		for x in range(len(board[y])):
			horizontalHs.append(node2dList[y][x].h)
		print(horizontalHs)

<<<<<<< HEAD
#This sets up the board as it is given in the textfiles
def setupBoard():
	fname = 'board-1-1.txt'
=======
def setupBoard(fname):
>>>>>>> origin/master
	with open(fname) as f:
		board = f.read().splitlines()
	return(board)

#This function computes the Manhatten distance from A to B
def getManhattanH(x, y):
	return abs(endPos[0] - x) + abs(endPos[1] - y)

#def getEuclidianH(x, y):
	#TODO easy later/not needed, we only use manhattan distance 

#This function creates all the initial nodes and puts it in a list system, depending on if its a wall, the start point, end point, or just open nodes.
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
			elif (board[y][x] == "B"):
				wall = False
				endPos = True
			horizontalNodeList.append(Node((x, y), h, g, wall, endPos, parent))
		verticalNodeList.append(horizontalNodeList)
	return verticalNodeList	

#This funstion gives each node its children, on evry side of the node
def setupChildrenOfNode(parentNode):
	#sets up the children to the left(west)
	if parentNode.pos[0] != 0: 
		westNode = node2dList[parentNode.pos[1]][parentNode.pos[0] - 1]
		reCheckNode(westNode, parentNode)
		if (westNode.endPos):
			return westNode

	#sets up the children upwards(north)
	if parentNode.pos[1] != 0:
		northNode = node2dList[parentNode.pos[1] - 1][parentNode.pos[0]]
		reCheckNode(northNode, parentNode)
		if (northNode.endPos):
			return northNode

	#sets up the children downwards(south)		
	if parentNode.pos[1] < (len(node2dList) - 1):
		southNode = node2dList[parentNode.pos[1] + 1][parentNode.pos[0]]
		reCheckNode(southNode, parentNode)
		if (southNode.endPos):
			return southNode

	#sets up the children to the right(east)		
	if parentNode.pos[0] < (len(node2dList[parentNode.pos[1]]) - 1):
		eastNode = node2dList[parentNode.pos[1]][parentNode.pos[0] + 1]
		reCheckNode(eastNode, parentNode)
		if (eastNode.endPos):
			return (eastNode)
	return None

#Checks node that hasent been discovered yet
def reCheckNode(node, parentNode):
	if (node.wall == False and (node not in closedList and node not in openList)): 
			if ((parentNode.g + 1) < node.g):
				node.parent = parentNode
				node.g = 1 + parentNode.g
			openList.append(node)

#Goes through the list of all discovered nodes and picks the one with the lowes cost
def getBestNodeInOpenList():
	bestNode = openList[0]
	for node in openList:
		if (node.g + node.h) < (bestNode.g + bestNode.h):
			bestNode = node
	return bestNode

#Prints the open and closed list we have made. Openlist are nodes who have been discovered but not visited, and closedlist ar nodes you once visited because you thought it was the best
def printLists():
	oListPos = []
	for pos in openList:
		oListPos.append(pos.pos)
	print(oListPos)
	cListPos = []
	for poss in closedList:
		cListPos.append(poss.pos)
	print(cListPos)

<<<<<<< HEAD
#makes the board with all nodes
board = setupBoard() # (y, x)
=======

fname = 'board-1-1.txt'
board = setupBoard(fname) # (y, x)
>>>>>>> origin/master
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

#moves the best node from openlist and appends it in the closedlist
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








