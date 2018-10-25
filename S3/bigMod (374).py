import sys

# Modular exponentiation
# Calculating the raw number is far too difficult. Therefore another approach is needed
# Since a^b mod N = (a^(b/c) mod N)^c (substitution rule), we can use D&C to reduce the 
# exponent and perform the modulo steps intermediate.
# (the intermediate numbers are way simpler to work with)

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
		B = int(line)
	elif i == 1:
		P = int(line)
	elif i == 2:
		M = int(line)
		sys.stdout.write("%d\n" % modexp(B, P, M))

	i = (i + 1) % 4
