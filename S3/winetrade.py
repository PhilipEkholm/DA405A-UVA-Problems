import sys

i = 0
numberOfHouses = 0
minWork = 0

def same_sign(a, b):
	return ((a < 0) == (b < 0))

def minimumWorkSlow(houses):
	work = 0

	for i in range(0, len(houses)):
		if houses[i] == 0:
			continue

		j = i
		while(houses[i] != 0):
			if not same_sign(houses[i], houses[j]) and houses[j] != 0:
				maxTrade = min(abs(houses[i]), abs(houses[j]))

				if houses[i] > houses[j]:
					houses[i] -= maxTrade
					houses[j] += maxTrade
				elif houses[i] < houses[j]:
					houses[i] += maxTrade
					houses[j] -= maxTrade

				work += maxTrade * (j - i)
				
			j += 1

	return work

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
