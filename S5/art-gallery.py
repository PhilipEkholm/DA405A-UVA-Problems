import sys

# After while you realize that finding a critical point in the gallery is equivalent to
# checking if the polygon (the gallery) formout is convex or concave. If it's concave, then
# there's at least one concave point which is wider than 180 degrees (which allows for a critical point)
#
# Equivalently, checking if a polygon is convex is the same thing as checking if only right 
# turns or left turns are made after each point. This can be checked by creating two vectors between
# three points and find the vector (cross) product. If the product is > 0 it's a left turn,
# otherwise right turn. Check this for all points in the polygon.

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

	def __str__(self):
		return "(" + str(self.x) + ", " + str(self.y) +")"

class Segment:
	def __init__(self, p, q):
		self.p1 = p
		self.p2 = q

	def leftTurn(self, segmentInFront):
		#Segments are assumed to have a common point (self.p2 == segmentInFront.p1)
		p = self.p1
		q = self.p2
		r = segmentInFront.p2

		rotation = (q.x - p.x) * (r.y - p.y) - (r.x - p.x) * (q.y - p.y)

		if rotation > 0:
			return True
		else:
			return False

	def __str__(self):
		return str(self.p1) + " to " + str(self.p2)

points = list()
polygon = list()
numberOfPoints = int(sys.stdin.readline().rstrip())
anyRightTurns = False
anyLeftTurns = False

while (numberOfPoints != 0):
	for i in range(0, numberOfPoints):
		x, y = [int(s) for s in sys.stdin.readline().split()]
		points.append(Point(x, y))

	points.append(points[0])
	points.append(points[1])

	for i in range(1, numberOfPoints + 2):
		polygon.append(Segment(points[i - 1], points[i]))

	for i in range(0, numberOfPoints):
		turnedLeft = polygon[i].leftTurn(polygon[i + 1])

		if turnedLeft:
			anyLeftTurns = True
		else:
			anyRightTurns = True

	#Yes if they have a critical point (only one type of turn can be made)
	if anyRightTurns ^ anyLeftTurns:
		print("No")
	else:
		print("Yes")

	numberOfPoints = int(sys.stdin.readline().rstrip())
	polygon.clear()
	points.clear()
	anyLeftTurns = False
	anyRightTurns = False
