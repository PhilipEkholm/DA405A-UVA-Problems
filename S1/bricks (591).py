from sys import stdin

# 1. Read the different heights of different stacks
# 2. Calculate average height, this will be the brick height for each stack
# 3. Calculate the difference between each stack and avg. height. 
# The absolute sum of these values will be the minimum number of moves required

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
