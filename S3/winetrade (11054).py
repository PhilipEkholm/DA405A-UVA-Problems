import sys

# The simplest problem due to the linearity of the problem and the fact that
# the demand exactly meets the supply. Because of this we can solve it by:
#
# 1. Read the number of houses and supply/order for each house
# 2. from house N move the value of house N to N + 1
# 3. Repeat (2) until reached house M - 1
# 4. The total amount of work = the sum of absolute value of each value move

i = 0
numberOfHouses = 0

def minimumWork(houses):
	work = 0

	for i in range(1, len(houses)):
		houses[i] += houses[i - 1]
		work += abs(houses[i - 1])

	return work

for line in sys.stdin:
	if line.rstrip() == "0":
		break
	elif i == 0:
		numberOfHouses = int(line)
	elif i == 1:
		houses = [int(s) for s in line.split()]
		print(minimumWork(houses))

	i = (i + 1) % 2
