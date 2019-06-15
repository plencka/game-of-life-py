#Paulina Lencka III THI GoLPyEntity, based on Conway's Game of Life
import threading, time, os, GoLEntities, colorama, msvcrt, GoLSpawnSet, GoLConfig
from copy import deepcopy

globalStop = True
clear = lambda: os.system('cls')

class cell:
	def __init__(self,state):
		self.state = state

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
	bSymbol = GoLConfig.Config()
	if isCorrect(h+dir[0],w+dir[1],gameProp):
		if board[h+dir[0]][w+dir[1]] == bSymbol.alive:
			return number+1
	return number

def checkForNeighbours(y,i, board, gameProp, state,tempBoard):
	h = y
	w = i
	sourceCell = cell(state)
	cfg = GoLConfig.Config()
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
	if sourceCell.state == 0 and number==cfg.ressurectThresh:
		tempBoard[h][w] = cfg.alive
	if sourceCell.state == 1:
		if number<cfg.stayAliveMin or number>cfg.stayAliveMax:
			tempBoard[h][w] = cfg.dead
	return tempBoard

def parseCells(gameProp, board):
	bS = GoLConfig.Config()
	tempBoard = deepcopy(board)
	for y in range(0,gameProp.height):
		for i in range(0,gameProp.width):
			cState = 0
			if board[y][i]==bS.alive:
				cState = 1
			tempBoard = list(checkForNeighbours(y,i,board,gameProp,cState,tempBoard))
	board = list(tempBoard)
	return board

def createBoard(gameProp):
	board = []
	for i in range(0,gameProp.height):
		board.append([gameProp.dead] * gameProp.width)
	return board

def drawBoard(board, gameProp):
	clear()
	for y in range(0,gameProp.height):
		for i in range(0,gameProp.width):
			print(board[y][i], end='')
		print()
		
#--------------------------GAME--------------------------
def exitState(gameProp):
	time.sleep(gameProp.timer+1)
	wait = input("Every thread resolved successfully. Press any key to exit.")

def playerInputNoWait(gameProp):
	global globalStop
	noWait = msvcrt.getch()
	globalStop=False

def runSim():
	cycleCount = 0
	gameProp = GoLConfig.Config()
	board = createBoard(gameProp)
	GoLSpawnSet.insertCells(board, gameProp)
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