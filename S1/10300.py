from sys import stdin

testCases = 0
cash = 0
count = 0
farmers = 0

for line in stdin:
	if testCases == 0:
		testCases = int(line)
		continue

	if farmers == 0:
		farmers = int(line)
	else:
		area, animals, enIndex = [int(s) for s in line.split()]
		cash += area * enIndex
		count += 1

		if count == farmers:
			print(cash)
			count = cash = farmers = 0
