#Component of GoLPyEntities. Configuration file.
class Config:
	dead = "\033[34m" + "█" + '\033[0m'
	alive = "\033[92m" + "ῼ" + '\033[0m'
	height = 25 #X 0 - height-1 //25 default
	width = 50 #Y 0 - width-1 //50 default
	timer = 0.3 #0.3 default
	ressurectThresh = 3 #3 default
	stayAliveMin = 2 #2 default
	stayAliveMax = 3 #3 default