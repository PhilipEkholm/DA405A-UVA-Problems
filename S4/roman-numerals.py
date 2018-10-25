import sys

# Basically two problems, being:
#
# 1. To calculate if the terms equal a valid roman sum
# 2. Find out if the signs could work as a possible arabic encoding
#
# Solving (1) is relatively easy. Add and sum together the value of 
# each roman character, unless the sign is in a 'negative position', where
# you subtract from the sum.
#
# Solving (2) is harder but basically works that you try all possible combinations.
# Count the number of different signs and give each one a value and try if it works, then increment
# and repeat for all signs. If there's no valid way of doing this it's 'impossible'.
# If there is one way of doing it then it's a valid encoding.
# If there is more than one way of doing it then it's ambiguous.


arabicEncodingSolutions = 0
leftPart = ""
rightPart = ""
firstTerm = ""
secondTerm = ""

def decode(romanNumber):
	romanSigns = {
		"I": 1,
		"V": 5,
		"X": 10,
		"L": 50,
		"C": 100,
		"D": 500,
		"M": 1000
	}

	result = 0

	for i in range(len(romanNumber) - 1):
		if romanSigns[romanNumber[i]] < romanSigns[romanNumber[i + 1]]:
			result -= romanSigns[romanNumber[i]]
		else:
			result += romanSigns[romanNumber[i]]

	#Add last roman symbol
	result += romanSigns[romanNumber[len(romanNumber) - 1]]

	return result

def getCharacters(numerals):
	charactersInTestcase = []

	for character in numerals:
		if charactersInTestcase.count(character) == 0:
			charactersInTestcase.append(character)

	return sorted(charactersInTestcase)

def solveArabicEncoding(current, allCharacters, value, used, head):
	global arabicEncodingSolutions, leftPart, rightPart, firstTerm, secondTerm

	if arabicEncodingSolutions > 1:
		return 0

	if current == len(allCharacters):
		n1 = n2 = n3 = 0

		for letter in firstTerm:
			n1 = 10 * n1 + value[letter]

		for letter in secondTerm:
			n2 = 10 * n2 + value[letter]

		for letter in rightPart:
			n3 = 10 * n3 + value[letter]

		if (n1 + n2) == n3:
			arabicEncodingSolutions += 1

		return 0

	flag = head[allCharacters[current]]
	d = 1 if flag else 0

	while(d < 10 and arabicEncodingSolutions < 2):
		if not used[d]:
			value[allCharacters[current]] = d
			used[d] = True
			solveArabicEncoding(current + 1, allCharacters, value, used, head)
			used[d] = False

		d += 1


while True:
	line = sys.stdin.readline().rstrip()

	if line == "#":
		break

	leftPart, rightPart = [s for s in line.split("=")]
	firstTerm, secondTerm = [term for term in leftPart.split("+")]

	charactersInTestcase = getCharacters(firstTerm + secondTerm + rightPart)

	head = {}
	value = {}

	for item in charactersInTestcase:
		value[item] = 0
		head[item] = False

	head[firstTerm[0]]  = True
	head[secondTerm[0]] = True
	head[rightPart[0]]  = True

	used = [False for s in range(128)]
	arabicEncodingSolutions = 0

	solveArabicEncoding(0, charactersInTestcase, value, used, head)

	res = ""

	romanSum = decode(firstTerm) + decode(secondTerm)

	if romanSum == decode(rightPart):
		res += "Correct "
	else:
		res += "Incorrect "

	if arabicEncodingSolutions == 0:
		res += "impossible"
	elif arabicEncodingSolutions == 1:
		res += "valid"
	else:
		res += "ambiguous"


	print(res)







