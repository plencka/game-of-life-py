import threading, time, os, GoLEntities, msvcrt
from copy import deepcopy

globalStop = True
clear = lambda: os.system('cls')
#LOGIC
class boardSymbols:
	dead = "_"
	alive = "#"

class cell:
	def __init__(self,state):
		self.state = state

class gameDefinition:
	def __init__(self, height, width, timer):
		self.height = height #X 0 - height-1
		self.width = width #Y 0 - width-1
		self.timer = timer

class neighbour:
	left = [0,-1]
	right = [0,1]
	up = [-1,0]
	down = [1,0]
	upLeft = [-1,-1]
	downLeft = [1,-1]
	upRight = [-1,1]
	downRight = [1,1]

def isCorrect(x,y, gameProp):
	if x>=0 and y>=0:
		if x<gameProp.height-1 and y<gameProp.width-1:
			return True
		else:
			return False
	else:
		return False

def checkCell(h,w,dir,gameProp,number,board):
	bSymbol = boardSymbols()
	if isCorrect(h+dir[0],w+dir[1],gameProp):
		if board[h+dir[0]][w+dir[1]] == bSymbol.alive:
			return number+1
	return number

def checkForNeighbours(y,i, board, gameProp, state,tempBoard):
	h = y
	w = i
	sourceCell = cell(state)
	bSymbol = boardSymbols()
	n = neighbour()
	number = 0
	number = checkCell(h,w,n.left,gameProp,number,board)
	number = checkCell(h,w,n.right,gameProp,number,board)
	number = checkCell(h,w,n.up,gameProp,number,board)
	number = checkCell(h,w,n.down,gameProp,number,board)
	number = checkCell(h,w,n.upLeft,gameProp,number,board)
	number = checkCell(h,w,n.downLeft,gameProp,number,board)
	number = checkCell(h,w,n.upRight,gameProp,number,board)
	number = checkCell(h,w,n.downRight,gameProp,number,board)
	if sourceCell.state == 0 and number==3:
		tempBoard[h][w] = bSymbol.alive
	if sourceCell.state == 1:
		if number<2 or number>3:
			tempBoard[h][w] = bSymbol.dead
	return tempBoard

def parseCells(gameProp, board):
	bS = boardSymbols()
	tempBoard = deepcopy(board)
	for y in range(0,gameProp.height):
		for i in range(0,gameProp.width):
			cState = 0
			if board[y][i]==bS.alive:
				cState = 1
			tempBoard = list(checkForNeighbours(y,i,board,gameProp,cState,tempBoard))
	board = list(tempBoard)
	return board

def createBoard(gameProp, elements):
	board = []
	for i in range(0,gameProp.height):
		board.append([elements.dead] * gameProp.width)
	return board

def drawBoard(board, gameProp):
	clear()
	for y in range(0,gameProp.height):
		for i in range(0,gameProp.width):
			print(board[y][i], end='')
		print()

def spawnEntity(entity, board, gameProp):
	bS = boardSymbols()
	k = bS.alive
	for i in range(0, entity.l):
		if (entity.pos[i][0]>=0 and entity.pos[i][0]<gameProp.height) and ((entity.pos[i][1]>=0 and entity.pos[i][1]<gameProp.width)):
			board[entity.pos[i][0]][entity.pos[i][1]] = k

#BOARD
def insertCells(board, gameProp):
	bS = boardSymbols()
	k = bS.alive
	spawnEntity(GoLEntities.eBlink(5,4), board, gameProp)
	spawnEntity(GoLEntities.eBlink(15,20), board, gameProp)
	spawnEntity(GoLEntities.eFlyer(7,7), board, gameProp)
	spawnEntity(GoLEntities.eFlyer(12,18), board, gameProp)
	spawnEntity(GoLEntities.eBush(14,35), board, gameProp)
	spawnEntity(GoLEntities.eGrower(5,35), board, gameProp)
	return board

#GAME
def exitState(gameProp):
	time.sleep(gameProp.timer+1)
	wait = input("Every thread resolved successfully. Press any key to exit.")
def playerInputNoWait(gameProp):
	global globalStop
	noWait = msvcrt.getch()
	globalStop=False

def runSim():
	cycleCount = 0
	gameProp = gameDefinition(25,50,1.15)
	elements = boardSymbols()
	board = createBoard(gameProp, elements)
	insertCells(board, gameProp)
	input = threading.Thread(target=playerInputNoWait, args=(gameProp,))
	input.start()
	while globalStop==True:
		drawBoard(board, gameProp)
		print("Cycles: ",cycleCount)
		cycleCount=cycleCount+1
		print("Press any key to stop simulation.")
		board = parseCells(gameProp,board)
		time.sleep(gameProp.timer)
	exitState(gameProp)

def main():
    runSim()

if __name__ == "__main__":
    main()