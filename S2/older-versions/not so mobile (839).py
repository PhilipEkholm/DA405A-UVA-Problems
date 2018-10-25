import sys

testCases = 0
balanced = True

line = sys.stdin.readline().rstrip()

def goDown():
	global balanced
	line = sys.stdin.readline().rstrip()

	wl, dl, wr, dr = [int(s) for s in line.split()]

	if wl == 0:
		wl = goDown()

	if wr == 0:
		wr = goDown()

	if (wl*dl != wr*dr):
		balanced = False

	return (wl + wr)


testCases = int(line)

while testCases:
	testCases -= 1
	balanced = True

	#get rid of blank line between testcases and cases
	sys.stdin.readline().rstrip()
	goDown()
	
	if balanced:
		sys.stdout.write("YES\n")
	else:
		sys.stdout.write("NO\n")

	if (testCases):
		sys.stdout.write("\n")



