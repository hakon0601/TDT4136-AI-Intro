
"""
H (Heuristic) = Distance to goal (through walls)
G (Movement Cost) = Value of movement. 1 in the first task
F = G + H
"""
import math

class Node:
	def __init__(self, h, g, wall, endPos, parent):
		self.h = h
		self.g = g
		self.f = h + g
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

def setupBoard():
	fname = 'board-1-1.txt'
	with open(fname) as f:
  		board = f.read().splitlines()
  	return(board)

def getManhattanH(x, y):
	return abs(endPos[0] - x) + abs(endPos[1] - y)

def getEuclidianH(x, y):
	#TODO easy later

def createInitialNodes():
	verticalNodeList = [] 
	for y in range(len(board)):
		horizontalNodeList = [] 		
		for x in range(len(board[y])):
			h = getManhattanH(x, y)
			g = 0
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
			horizontalNodeList.append(Node(h, g, wall, endPos))
		verticalNodeList.append(horizontalNodeList)
	return verticalNodeList	


def setupInitialParents():
	if startPos[0] != 0: 
		# Adding startnode as parent of the west-node
		node2dList[startPos[1]][startPos[0] - 1].parent = startNode
	if startPos[1] != 0:
		#North
		node2dList[startPos[1] - 1][startPos[0]].parent = startNode
	if startPos[1] < (len(node2dList) - 1):
		#South
		node2dList[startPos[1] + 1][startPos[0]].parent = startNode
	if startPos[0] < (len(node2dList[startPos[1]]) - 1):
		#East
		node2dList[startPos[1]][startPos[0] + 1].parent = startNode
		
board = setupBoard() # (y, x)
startPos = getPosOf("A") # (x, y)
endPos = getPosOf("B") # (x, y)
node2dList = createInitialNodes() # (y, x)...
startNode = node2dList[startPos[1]][startPos[0]]

printBoard()

closedList = []
openList = []

closedList.append(startNode) #Adding the startnode to the closed list






