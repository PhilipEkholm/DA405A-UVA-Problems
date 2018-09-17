import sys

i = 0

def modexp(x, y, N):
	if y == 0:
		return 1
	z = modexp(x, int(y/2), N)

	if y % 2 == 0:
		return (z**2 % N)
	else:
		return ((x*(z**2)) % N)
	
for line in sys.stdin:
	if i == 0:
		x = int(line)
	elif i == 1:
		y = int(line)
	elif i == 2:
		N = int(line)
		sys.stdout.write("%d\n" % modexp(x, y, N))

	i = (i + 1) % 4