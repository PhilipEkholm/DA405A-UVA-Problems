import sys

class Edge:
	def __init__(self, i, j):
		self.i = i
		self.j = j

	def __str__(self):
		return "(" + str(self.i) + ", " + str(self.j) + ")"

def printBestRoute(bestRoute):
	res = str(bestRoute)
	print(res[1:len(res) - 1].replace(",", ""))

for line in sys.stdin:
	rows, cols = [int(s) for s in line.split()]
	field = [[0 for i in range(cols)] for j in range(rows)]
	cost = [[0 for i in range(cols)] for j in range(rows)]
	routeTable = [[None for i in range(cols)] for j in range(rows)]

	for i in range(rows):
		matrix = []
		line2 = sys.stdin.readline()

		for number in line2.split():
			matrix.append(int(number))

	print(matrix)

	elementIndex = 0

	for i in range(rows):
		for j in range(cols):
			if elementIndex < len(matrix):
				field[i][j] = matrix[elementIndex]
				cost[i][cols - 1] = field[i][cols - 1]
				elementIndex += 1

	'''while i < rows:
		rowLine = [int(s) for s in sys.stdin.readline().split()]

		#Special case: two rows on the same fucking line...
		if len(rowLine) > cols:
			field[i] = rowLine[0:cols]
			cost[i][cols - 1] = field[i][cols - 1]
			i += 1
			field[i] = rowLine[cols:]
			cost[i][cols - 1] = field[i][cols - 1]
		else:
			field[i] = rowLine
			cost[i][cols - 1] = field[i][cols - 1]

		i += 1'''


	for j in range(cols - 2, -1, -1):
		for i in range(rows):
			lowestValue = min(
				cost[(i - 1) % rows][j + 1],
				cost[i % rows][j + 1],
				cost[(i + 1) % rows][j + 1],)

			#An extra condition needs to be fulfilled if you want to do it in lexicographical order
			if lowestValue == cost[(i - 1) % rows][j + 1] and (i - 1) % rows != rows - 1:
				routeTable[i][j] = Edge((i - 1) % rows, j + 1)
			elif lowestValue == cost[(i) % rows][j + 1]:
				routeTable[i][j] = Edge((i) % rows, j + 1)
			elif lowestValue == cost[(i + 1) % rows][j + 1]:
				routeTable[i][j] = Edge((i + 1) % rows, j + 1)
			elif lowestValue == cost[(i - 1) % rows][j + 1]:
				routeTable[i][j] = Edge((i - 1) % rows, j + 1)

			cost[i][j] = field[i][j] + cost[routeTable[i][j].i][routeTable[i][j].j]

	minimumWeight = cost[0][0]
	startRow = 0

	for i in range(rows):
		if minimumWeight > cost[i][0]:
			minimumWeight = cost[i][0]
			startRow = i

	bestRoute = [startRow + 1]

	for k in range(0, cols - 1):
		if k == 0:
			m = routeTable[startRow][k].i
		else:
			m = routeTable[m][k].i

		bestRoute.append(m + 1)

	printBestRoute(bestRoute)
	print(minimumWeight)




	




