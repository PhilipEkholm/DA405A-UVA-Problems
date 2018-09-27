import sys
import math

numberOfSets = 0
points = list()
count = -1

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

def getEuclidDistance(p, q):
	return math.sqrt((q.x - p.x)**2 + (q.y - p.y)**2)

def closestPair(P):
	minDist = float("inf")

	for i in range(0, len(P)-1):
		for j in range(i + 1, len(P)):
			p = P[i]
			q = P[j]

			d = getEuclidDistance(p, q)
			if d < minDist:
				minDist = d

	return minDist

for line in sys.stdin:
	if count == -1:
		numberOfSets =  int(line.rstrip())
	elif count != -1:
		x, y = [int(s) for s in line.split()]
		points.append(Point(x, y))
	
	count += 1

	if count == numberOfSets and numberOfSets != 0:
		closest = closestPair(points)
		if closest < 10000:
			print(format(closest, ".4f"))
		else:
			print("INFINITY")

		points = list()
		count = -1
