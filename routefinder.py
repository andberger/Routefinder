import sys
import pandas as pd
from pqdict import PQDict
from sets import Set
import numpy as np


class Problem:
	initState = None
	goalState = None
	datapath = None

class Node:
	def __init__(self,state=None,parent=None,action=None,pathcost=None):
		if state is not None:
			self.state = state
		else:
			self.state = None
		if parent is not None:
			self.parent = parent
		else:
			self.parent = None
		if action is not None:
			self.action = action
		else:
			self.action = action
		if pathcost is not None:
			self.pathcost = pathcost
		else:
			self.pathcost = None


def readFunc(dataLocation):
	listoflists = list()
	read = pd.read_csv(dataLocation,sep=" ",header=None)
	for i in range(read.count()[0]):
		rowlist = read.iloc[i,:].tolist()
		listoflists.append(rowlist)
	return listoflists


def findPossibleActions(state,data):
	listOfActions = list()
	for i in range(len(data)):
		if tuple(data[i][0:2]) == state:
			listOfActions.append(data[i][2])
	return listOfActions


def childNode(problem, parent, action, data):
	node = Node()
	for i in range(len(data)):
		if tuple(data[i][0:2]) == parent.state and data[i][2] == action:
			node.state = tuple(data[i][3:5])
			node.parent = parent
			node.action = action
			node.pathcost = f(parent, node, problem.goalState)
	return node


#Path cost with heuristic function h, where h is the straight line distance to the goal.
def f(n1,n2,goal):
	return g(n1,n2) + h(n2,goal)
def g(n1,n2):
	euclideanDist = np.sqrt(np.power((n2.state[0]-n1.state[0]),2) + np.power((n2.state[1]-n1.state[1]),2))
	if type(n1.parent) != type(None):
		totalDist = g(n1.parent, n1) + euclideanDist
	else:
		totalDist = euclideanDist
	return totalDist
def h(n,goal):
	distToGoal = np.sqrt(np.power((goal[0]-n.state[0]),2) + np.power((goal[1]-n.state[1]),2))
	return distToGoal


def solution(node,problem):
	route = list()
	currNode = node
	while currNode.state != problem.initState:
		route.append(currNode.action)
		currNode = currNode.parent
	route.reverse()
	return tuple((route, node.pathcost))





def AStar(problem):
	#Give path of data file
	path = problem.datapath
	#Data
	data = list()
	data = readFunc(path)

	#Initialization of a node.
	node = Node()
	node.state = problem.initState
	node.pathcost = 0

	#Frontier is a priority queue dict of tuples:(node.pathcost, node), with key:node.state
	#Frontier is ordered by path cost.
	frontier = PQDict()
	frontier.additem(node.state, (node.pathcost,node))

	#Explored begins as the empty set.
	explored = Set()

	while True:
		if len(frontier) == 0:
			return 'No route exists'
		node = frontier.popitem()[1][1] #Chooses the lowest-cost node in frontier
		if problem.goalState == node.state:
			return solution(node,problem)
		explored.add(node.state)

		possibleActions = findPossibleActions(node.state,data)
		for action in range(len(possibleActions)):
			child = childNode(problem,node,possibleActions[action],data)
			if (child.state not in explored) and (child.state not in frontier):
				frontier.additem(child.state, (child.pathcost, child))
			elif (child.state in frontier) and (frontier[child.state][1].pathcost > child.pathcost):
				frontier[child.state] = (child.pathcost, child)
