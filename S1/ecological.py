from sys import stdin

# Algorithm: real simple
# 1. read all variables from stdin
# 2. the total amount of cash = area * environmental index.
# No information about the animals is needed

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

