import sys

def isSubsequence(subs, seq):
	if len(subs) > len(seq):
		return "No"

	for i in range(0, len(subs)):
		while subs[i] != seq[i] and len(seq) > len(subs):
			seq = seq[:i] + seq[i + 1:]
			

		if seq[:i + 1] == subs:
			return "Yes"


	return "No"

for line in sys.stdin:
	subsequence, sequence = [s for s in line.split()]
	print(isSubsequence(subsequence, sequence))
