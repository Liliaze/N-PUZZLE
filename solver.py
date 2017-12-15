from node import Node
from state import State
from prioritySet import PrioritySet
from heapq import heappush, heappop
import algo
import heuristic
import sys
import checkIsSolvable



# Classe principale de projet
# contient une fonction pour parser : parser (voir fichier parser.py)
# contient une fonction pour resoudre le puzzle : algo (A FAIRE)
# contient une fonction heuristique : algo (A FAIRE)
# contient une liste de toutes les grilles pouvant etre choisi : openend (voir classe Node)
# contient une liste de toutes les grilles ayant deja ete choisi : closed (voir classe Node)
# contient la grille actuellement selectionne : actual (voir classe Node)
# contient la taille de la grille : size

class Solver:
	
	#penser à ajouter ici les noms des nouveau algo, l'appel à la fonction et "True" si utilise des heuristiques sinon "False"
	algoList = [
		["A*", algo.astar, True],
		["Uniform Cost Search", algo.uniform, False],
		["Greedy Search", algo.greedy, True]
		]
	
	#penser à ajouter ici les noms des nouveaux heuristiques et leur appel a fonction
	heuristicList = [
		["Euclidean Distance", heuristic.euclideanDistance],
		["Manhattan Distance", heuristic.manhattanDistance],
		["Misplaced Tiles", heuristic.misplacedTiles],
		["Misplaced Tiles + Manhattan Distance", heuristic.misplacedTilesAndManhattan],
		["Out Of Row And Column", heuristic.outOfRowAndColumn],
		["Manhattan Distance + Linear Conflict", heuristic.manhattanLinearConflict]
		]
	
	def __init__(self, parser):
		msg = """\033[1;31m
		╦ ╦╔═╗╦  ╔═╗╔═╗╔╦╗╔═╗    ╦╔╗╔    ╔╗╔   ╔═╗╦ ╦╔═╗╔═╗╦  ╔═╗ 
		║║║║╣ ║  ║  ║ ║║║║║╣     ║║║║    ║║║───╠═╝║ ║╔═╝╔═╝║  ║╣  
		╚╩╝╚═╝╩═╝╚═╝╚═╝╩ ╩╚═╝    ╩╝╚╝    ╝╚╝   ╩  ╚═╝╚═╝╚═╝╩═╝╚═╝ 
		╔╗ ╦ ╦    ╔╦╗╔═╗╦═╗╦  ╦╔╗╔    ╔═╗╔╗╔╔╦╗    ╔╦╗╦╔═╗╔╗╔╔═╗
		╠╩╗╚╦╝    ║║║║╣ ╠╦╝║  ║║║║    ╠═╣║║║ ║║     ║║║╠═╣║║║╠═╣
		╚═╝ ╩     ╩ ╩╚═╝╩╚═╩═╝╩╝╚╝    ╩ ╩╝╚╝═╩╝    ═╩╝╩╩ ╩╝╚╝╩ ╩
		\033[m"""
		print(msg)
		Node.solver = self
		State.solver = self
		self.parser = parser
		self.getDistance = algo.getDistanceAstar

	def sayGoodbye(self):
		msg = """\033[1;36m
╔═╗╔═╗╔═╗╔╦╗  ╔╗ ╦ ╦╔═╗  ╔═╗╔╗╔╔╦╗  ╔╦╗╔═╗╦═╗╦═╗╦ ╦  ╔═╗╦ ╦╦═╗╦╔═╗╔╦╗╔╦╗╔═╗╔═╗
║ ╦║ ║║ ║ ║║  ╠╩╗╚╦╝║╣   ╠═╣║║║ ║║  ║║║║╣ ╠╦╝╠╦╝╚╦╝  ║  ╠═╣╠╦╝║╚═╗ ║ ║║║╠═╣╚═╗
╚═╝╚═╝╚═╝═╩╝  ╚═╝ ╩ ╚═╝  ╩ ╩╝╚╝═╩╝  ╩ ╩╚═╝╩╚═╩╚═ ╩   ╚═╝╩ ╩╩╚═╩╚═╝ ╩ ╩ ╩╩ ╩╚═╝
     *                                                          *
                                  *                  *        .--.
      \/ \/  \/  \/                                        ./   /=*
        \/     \/      *            *                ...  (_____)
         \ ^ ^/                                       \ \_((^o^))-.    *
         (o)(O)--)--------\.                           \   (   ) \ \._.
         |    |  ||================((~~~~~~~~~~~~~~~~~))|   ( )   |    \ 
          \__/             ,|        \. * * * * * * ./  (~~~~~~~~~~)    \ 
          *        ||^||\.____./|| |          \___________/     ~||~~~~|~'\____/ *
            || ||     || || A            ||    ||         ||    |   
     *      <> <>     <> <>          (___||____||_____)  ((~~~~~|   *
		\033[m"""
		print (msg)
	
	def askConfig(self):
		self.algo, needHeuristic = self.askAlgo()
		self.heuristic = self.askHeuristic(needHeuristic)
	
	def askAlgo(self):
		print("Choose your Algorrithm :")
		i = 0
		for name in self.algoList:
			print(str(i)+ " = " + name[0])
			i += 1
		while (True):
			try:
				algoInput = int(input("Number : "))
			except EOFError:
				print("\033[1;31mDon't try this please")
				exit()
			except:
				continue
			if (0 <= algoInput < i):
				return(self.algoList[algoInput][1], self.algoList[algoInput][2])
	
	def askHeuristic(self, needHeuristic):
		if (needHeuristic == True):
			print("\nA heuristic function is necessary, choose one : ")
			i = 0
			for name in self.heuristicList:
				print(str(i)+ " = " + name[0])
				i += 1
			while (True):
				try:
					heuristicInput = int(input("Number : "))
				except EOFError:
					print("\033[1;31mDon't try this please")
					exit()
				except:
					continue
				if (0 <= heuristicInput < i):
					return(self.heuristicList[heuristicInput][1])
		else:
			print("Heuristic function is not necessary.")
			return(heuristic.defaultHeuristic)
	
	def askAgain(self):
		answer = "x"
		while not answer in 'yYnN':
			answer = input("\nDo you want to start again with the same grid ? Answer : 'Y' or 'N'.")
		return answer 
	
	def parseFile(self):
		self.size, self.first = self.parser()
		self.goal = State(self.getGoal(self.size))
		self.goal.rehash()
		self.actual = Node(None, State(self.first))
		self.actual.state.rehash()
		self.closed = set([self.actual])
#		self.opened = []
		self.opened = PrioritySet()
		self.actual.getAllPossibility(self.opened)
#		self.opened = self.actual.getAllPossibility()
	
	def reinit(self):
		self.goal = State(self.getGoal(self.size))
		self.goal.rehash()
		self.actual = Node(None, State(self.first))
		self.actual.state.rehash()
		self.closed = set([self.actual])
		self.opened = PrioritySet()
		self.actual.getAllPossibility(self.opened)
	
	def newTry(self):
		tmp = self.opened.pop()
		if tmp == None:
			return False
		self.closed.add(self.actual)
		self.actual = tmp
		return True

	def solve(self):
		print("\nResolution in progress, please wait...")
		if self.algo(self) == True:
			print("Puzzle solved !")
			return True
		else:
			print("Puzzle unsolvable.")
			return False

	def printNodes(self):
		print("\nACTUAL NODES:")
		print(str(self.actual.state.grid))
		print("\nCLOSED NODES:")
		for n in self.closed:
			print(str(n.state.grid))
		print("\nOPEN NODES:")
		for n in self.opened:
			print(str(n.state.grid))

	def printSolution(self):
		path, steps  = self.getPathFromStart(self.actual)
		for n in path:
			print(str(n.state.grid) + " heuristic cost = " + str(n.distanceFromEnd))
		print("number of steps : " + str(steps))
		print("complexity in size : " + str(len(self.opened) + len(self.closed)))
		print("complexity in time : " + str(len(self.closed)))

	def checkIsSolvable(self):
		check = checkIsSolvable.isSolvable(self.size, self.first, self.goal.grid)
		if (check == False):
			print("\033[1;31mSorry, this N-Puzzle is Unsolvable\033[m")
			self.sayGoodbye()
			exit()
		else:
			print ("\033[1;32mThis N-Puzzle is solvable\033[m")

	def start(self):
		answer = 'Y'
		self.askConfig()
		self.parseFile()
		self.checkIsSolvable()
		while answer in 'yY':
			if self.solve():
				self.printSolution()
			#self.printNodes()
			answer = self.askAgain()
			if answer in "yY":
				self.askConfig()
				self.reinit()
		self.sayGoodbye()
	
	def getPathFromStart(self, node):
		path = []
		step = 0
		while node != None:
			path.append(node)
			node = node.parent
			step += 1
		return (reversed(path), step)

	def getGoalPoint(self, n):
		return self.goalPoints[n]

	def getGoal(self, size):
		self.goalPoints = dict()
		solution = [[-1 for x in range(size)] for y in range(size)]
		x, y = 0, 0
		vx, vy = 1, 0
		value = list(range(1, size*size))
		value.append(0)
		for i in value:
			solution[y][x] = i
			self.goalPoints[i] = (y,x)
			x += vx
			y += vy
			if (y < 0 or x < 0 or x >= size or y >= size or solution[y][x] != -1):
				x -= vx
				y -= vy
				if (vx != 0):
					vy = vx
					vx = 0
				else:
					vx = vy * -1
					vy = 0
				x += vx
				y += vy
		print("GOAL : " + str(solution))
		return solution
			
#	def isSolved(self):
