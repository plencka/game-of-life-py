#Component of GoLPyEntities. Defines content on board.
#Entities are defined as classes within GoLEntities.py

import GoLEntities, GoLPyEntity, GoLConfig

def spawnEntity(entity, board, gameProp): #Get entity, check if element of entity is within borders, change board
	bS = GoLConfig.Config()
	k = bS.alive
	for i in range(0, entity.l): #Won't spawn outside bounds. Part of entities can spawn if few cells are within board.
		if (entity.pos[i][0]>=0 and entity.pos[i][0]<gameProp.height) and ((entity.pos[i][1]>=0 and entity.pos[i][1]<gameProp.width)):
			board[entity.pos[i][0]][entity.pos[i][1]] = k

def insertCells(board, gameProp): #Change board directly or by spawnEntity function.
	bS = GoLConfig.Config()
	k = bS.alive
	spawnEntity(GoLEntities.eGrower(10,23), board, gameProp)
	spawnEntity(GoLEntities.eFlower(5,15), board, gameProp)
	spawnEntity(GoLEntities.eFlyer(18,40), board, gameProp)
	spawnEntity(GoLEntities.eGrower(20,23), board, gameProp)
	#board[validHeight][validWidth] = k // for manual input, or define new entity in GoLEntities.py and spawn it using above function.
	return board