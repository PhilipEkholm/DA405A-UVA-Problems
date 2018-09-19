from sys import stdin

setNumber = 0
stacks = 0

for line in stdin:
	if line == "0\n":
		continue

	if stacks == 0:
		stacks = int(line)
		setNumber += 1
		continue

	heights = [int(h) for h in line.split()]
	sumOfBricks = sum(heights)
	avgHeight = sumOfBricks/stacks

	for i in range(0, len(heights)):
		heights[i] -= avgHeight

		if heights[i] < 0:
			heights[i] = 0

	minimumMoves = sum(heights)
	print("Set #%d" % setNumber)
	print("The minimum number of moves is %d.\n" % minimumMoves)
	stacks = 0
