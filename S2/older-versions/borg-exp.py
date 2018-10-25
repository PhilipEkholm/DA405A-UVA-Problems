import sys
import time
from collections import deque
#Testa att ta bort samtliga .get metoder

class DisjointedSet:
	def __init__(self, vertices):
		self.parents = {}
		self.ranks = {}

		for vertex in vertices:
			self.parents[vertex] = vertex
			self.ranks[vertex] = 0

	def find(self, vertex):
		if self.parents.get(vertex) == vertex:
			return vertex

		return self.find(self.parents.get(vertex))

	def union(self, firstSet, secondSet):
		if self.ranks.get(firstSet) > self.ranks.get(secondSet):
			self.parents[secondSet] = firstSet
		elif self.ranks.get(firstSet) < self.ranks.get(secondSet):
			self.parents[firstSet] = secondSet
		else:
			self.parents[firstSet] = secondSet
			self.ranks[secondSet] = self.ranks.get(secondSet) + 1

class Edge:
	def __init__(self, vertexFrom, vertexTo):
		self.vertexFrom = vertexFrom
		self.vertexTo   = vertexTo

	def equals(self, edge):
		duplicate = self.vertexFrom == edge.vertexFrom and self.vertexTo == edge.vertexTo
		negated = self.vertexFrom == edge.vertexTo and self.vertexTo == edge.vertexFrom

		return (duplicate or negated)


class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		self.allEdges = []

	def setWeights(self):
		vertexKeys = []

		for vertex in self.vertices.keys():
			if self.vertexValues.get(vertex) != " ":
				self.bfsSearch(vertex)
				vertexKeys.append(vertex)

		self.vertexKeys = vertexKeys

	def bfsSearch(self, rootVertice):
		vertexQueue = deque([])
		visited = [[False for i in range(self.cols)] for j in range(self.rows)]

		rowsAndCols = rootVertice.split(",")
		rootRows = int(rowsAndCols[0])
		rootCols = int(rowsAndCols[1])
		visited[rootRows][rootCols] = True

		vertexQueue.append(rootVertice)

		vertexDistance = {}
		vertexDistance[rootVertice] = 1

		while len(vertexQueue) > 0:
			current = vertexQueue.popleft()
			edges = self.vertices.get(current)

			for edge in edges:
				vertex = edge.vertexTo
				rowsAndCols = vertex.split(",")
				vertexRow = int(rowsAndCols[0])
				vertexCol = int(rowsAndCols[1])

				if not visited[vertexRow][vertexCol]:
					visited[vertexRow][vertexCol] = True
					vertexDistance[vertex] = (int(vertexDistance.get(current)) + 1)

					if (self.vertexValues.get(vertex) != " "):
						updatedEdge = Edge(rootVertice, vertex)
						updatedEdge.weight = int(vertexDistance.get(current))
						self.allEdges.append(updatedEdge)

					vertexQueue.append(vertex)

	def getMinCost(self):
		#Use Kruskal's algorithm and return min cost
		#sort edges using lambda function with weight in mind
		ds = DisjointedSet(self.vertexKeys)
		totalWeight = 0
		sortedEdges = sorted(self.allEdges, key=lambda edge: edge.weight)

		for edge in sortedEdges:
			firstParent = ds.find(edge.vertexFrom)
			secondParent = ds.find(edge.vertexTo)

			if firstParent != secondParent:
				totalWeight += edge.weight
				ds.union(firstParent, secondParent)

		return totalWeight

def convertMazeToGraph(maze):
	vertices = {}
	vertexValues = {}

	for i in range(0, len(maze)):
		for j in range(0, len(maze[i])):
			if maze[i][j] != "#" and maze[i][j] != "\n":
				edges = []
				vertexValues[str(i) + "," + str(j)] = maze[i][j]

				if (j - 1 > 0):
					if (maze[i][j - 1] != "#"):
						edges.append(Edge(str(i) + "," + str(j), str(i) + "," + str(j - 1)))

				if (i - 1 > 0):
					if (maze[i - 1][j] != "#"):
						edges.append(Edge(str(i) + "," + str(j), str(i - 1) + "," + str(j)))

				if (j + 1 < len(maze[i])):
					if (maze[i][j + 1] != "#"):
						edges.append(Edge(str(i) + "," + str(j), str(i) + "," + str(j + 1)))

				if (i + 1 < len(maze) and j + 1 < len(maze[i])):
					if (maze[i + 1][j] != "#"):
						edges.append(Edge(str(i) + "," + str(j), str(i + 1) + "," + str(j)))

				vertices[str(i) + "," + str(j)] = edges

	g = Graph(vertices)
	g.vertexValues = vertexValues

	return g

#Main code
testCases = int(sys.stdin.readline().rstrip())

for i in range(0, testCases):
	cols, rows = [int(s) for s in sys.stdin.readline().split()]
	maze = []

	for j in range(0, rows):
		maze.append(sys.stdin.readline())

	graph = convertMazeToGraph(maze)
	graph.rows = rows
	graph.cols = cols
	graph.setWeights()
	print(graph.getMinCost())





