import sys

#Maybe not use a different implementation than the one in friends (prev. assignment)
class DisjointedSet:
	def __init__(self, vertices):
		self.parents = {}
		self.ranks = {}

		for vertex in vertices.keys():
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

	def getVertexFrom(self):
		return self.vertexFrom

	def getVertexTo(self):
		return self.vertexTo

	def getWeight(self):
		return self.weight

	def setWeight(self, weight):
		self.weight = weight

	def __str__(self):
		return (self.vertexFrom + "--" + self.vertexTo + ", weight: " + str(self.weight))

class Graph:
	def __init__(self, vertices):
		self.vertices = vertices
		self.allEdges = []

	def setVertexValues(self, vertexValues):
		self.vertexValues = vertexValues

	def setRows(self, rows):
		self.rows = rows

	def setCols(self, cols):
		self.cols = cols

	def setWeights(self):
		updatedGraph = {}

		for vertex in self.vertices.keys():
			if self.vertexValues.get(vertex) != " ":
				updatedEdges = self.bfsSearch(vertex)
				updatedGraph[vertex] = updatedEdges

		self.vertices = updatedGraph.copy()

	def bfsSearch(self, rootVertice):
		vertexQueue = []
		visited = [[False for i in range(self.cols)] for j in range(self.rows)]

		rowsAndCols = rootVertice.split(",")
		rootRows = int(rowsAndCols[0])
		rootCols = int(rowsAndCols[1])
		visited[rootRows][rootCols] = True

		vertexQueue.insert(0,rootVertice)

		updatedEdges = []
		vertexDistance = {}
		vertexDistance[rootVertice] = 1

		while vertexQueue != []:
			current = vertexQueue.pop()
			edges = self.vertices.get(current)

			for edge in edges:
				vertex = edge.getVertexTo()
				rowsAndCols = vertex.split(",")
				vertexRow = int(rowsAndCols[0])
				vertexCol = int(rowsAndCols[1])

				if not visited[vertexRow][vertexCol]:
					visited[vertexRow][vertexCol] = True
					vertexDistance[vertex] = (int(vertexDistance.get(current)) + 1)

					if (self.vertexValues.get(vertex) != " "):
						updatedEdge = Edge(rootVertice, vertex)
						updatedEdge.setWeight(int(vertexDistance.get(current)))
						updatedEdges.append(updatedEdge)
						self.allEdges.append(updatedEdge)

					vertexQueue.insert(0, vertex)

		return updatedEdges

	def getMinCost(self):
		#Use Kruskal's algorithm and return min cost
		#sort edges using lambda function with weight in mind
		ds = DisjointedSet(self.vertices)
		totalWeight = 0
		sortedEdges = sorted(self.allEdges, key=lambda edge: edge.weight)

		for edge in sortedEdges:
			firstParent = ds.find(edge.getVertexFrom())
			secondParent = ds.find(edge.getVertexTo())

			if firstParent != secondParent:
				totalWeight += edge.getWeight()
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
	g.setVertexValues(vertexValues)

	return g

#Main code
testCases = int(sys.stdin.readline().rstrip())

for i in range(0, testCases):
	cols, rows = [int(s) for s in sys.stdin.readline().split()]
	maze = []

	for j in range(0, rows):
		maze.append(sys.stdin.readline())

	graph = convertMazeToGraph(maze)
	graph.setRows(rows)
	graph.setCols(cols)
	graph.setWeights()
	print(graph.getMinCost())

















