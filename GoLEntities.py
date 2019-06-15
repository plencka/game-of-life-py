#Component of GoLPyEntity.
#Predefined entities that can be placed on board using GoLSpawnSet.py

import time, os
class eBush:
	def __init__(self,offsetX,offsetY):
		self.l = 6
		self.pos = []
		self.pos.append([0+offsetX,0+offsetY])
		self.pos.append([0+offsetX,1+offsetY])
		self.pos.append([0+offsetX,2+offsetY])
		self.pos.append([1+offsetX,0+offsetY])
		self.pos.append([1+offsetX,1+offsetY])
		self.pos.append([1+offsetX,2+offsetY])
class eBlink:
	def __init__(self,offsetX,offsetY):
		self.l = 3
		self.pos = []
		self.pos.append([0+offsetX,0+offsetY])
		self.pos.append([0+offsetX,1+offsetY])
		self.pos.append([0+offsetX,2+offsetY])
class eFlyer:
	def __init__(self,offsetX,offsetY):
		self.l = 5
		self.pos = []
		self.pos.append([0+offsetX,0+offsetY])
		self.pos.append([0+offsetX,1+offsetY])
		self.pos.append([0+offsetX,2+offsetY])
		self.pos.append([1+offsetX,0+offsetY])
		self.pos.append([2+offsetX,1+offsetY])
		
class eGrower:
	def __init__(self,offsetX,offsetY):
		self.l = 6
		self.pos = []
		self.pos.append([0+offsetX,0+offsetY])
		self.pos.append([0+offsetX,1+offsetY])
		self.pos.append([0+offsetX,2+offsetY])
		self.pos.append([2+offsetX,0+offsetY])
		self.pos.append([1+offsetX,1+offsetY])
		self.pos.append([2+offsetX,2+offsetY])

class eFlower:
	def __init__(self,offsetX,offsetY):
		self.l = 8
		self.pos = []
		self.pos.append([0+offsetX,0+offsetY])
		self.pos.append([0+offsetX,2+offsetY])
		self.pos.append([0+offsetX,4+offsetY])
		self.pos.append([1+offsetX,1+offsetY])
		self.pos.append([1+offsetX,3+offsetY])
		self.pos.append([2+offsetX,0+offsetY])
		self.pos.append([2+offsetX,2+offsetY])
		self.pos.append([2+offsetX,4+offsetY])
class ePyramid:
	def __init__(self,offsetX,offsetY):
		self.l = 8
		self.pos = []
		self.pos.append([0+offsetX,2+offsetY])
		self.pos.append([1+offsetX,1+offsetY])
		self.pos.append([1+offsetX,3+offsetY])
		self.pos.append([2+offsetX,0+offsetY])
		self.pos.append([2+offsetX,1+offsetY])
		self.pos.append([2+offsetX,2+offsetY])
		self.pos.append([2+offsetX,3+offsetY])
		self.pos.append([2+offsetX,4+offsetY])