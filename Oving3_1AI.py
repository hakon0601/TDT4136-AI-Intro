
"""
H (Heuristic) = Distance to goal (through walls)
G (Movement Cost) = Value of movement. 1 in the first task
F = G + H
"""
import math

class Node:
	def __init__(self, h, g, wall, endPos):
		self.h = h
		self.g = h
		self.wall = wall
		self.endPos = endPos

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

def getH(x, y):
	return abs(endPos[0] - x) + abs(endPos[1] - y)

def createInitialNodes():
	verticalNodeList = [] 
	for y in range(len(board)):
		horizontalNodeList = [] 		
		for x in range(len(board[y])):
			h = getH(x, y)
			g = 0
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

		

board = setupBoard()
startPos = getPosOf("A")
endPos = getPosOf("B")
node2dList = createInitialNodes()

printBoard()

closedList = []
openList = []