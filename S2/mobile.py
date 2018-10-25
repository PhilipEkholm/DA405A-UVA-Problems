import sys

# After a while you realize that if the mobile is in equilibrium then the whole submobile
# is also in equilibrium. This allows for solving recursively. 
#
# 1. Assume from the start that the mobile is in equilibrium and read first line
# 2. If there's a submobile, read the next line and continue until you've reached a mobile
# 3. Check if the mobile is in equilibrium. If any submobile is not in equilibrium then it's
#    not balanced. Return the weight of the submobile and continue checking recursively.
# 4. (Obviously) print YES if it's balanced or NO otherwise.

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

