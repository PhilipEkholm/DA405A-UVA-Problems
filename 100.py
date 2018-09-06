from sys import stdin

L = 1000000
cycleCounts = [None]*L
cycleCounts[0] = 0
cycleCounts[1] = 1

def collatzCycles(n):
	if (n < L) and (cycleCounts[n] is not None):
		return (cycleCounts[n])

	if n % 2 == 1:
		return (1+collatzCycles(3 * n + 1))
	else:
		return (1+collatzCycles(int(n/2)))

for o in range(L):
	cycleCounts[o] = collatzCycles(o)

for line in stdin:
	i,j = [int(s) for s in line.split()]
	cycles = []

	for k in range(min(i,j), max(i,j) + 1):
		cycles.append(collatzCycles(k))

	print(i, j,max(cycles))
