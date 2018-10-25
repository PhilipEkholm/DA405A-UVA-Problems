import sys

# 1. Compare character N of the set and subset
# 2. If equal, compare next character. Else, trim away a character 
#    from sequence until they match or sequence is shorter than subsequence
# 3. Check if the sequence matches the subsequence. If so return yes, else repeat (1)
# 4. If you've ran though all characters in subset then it's not a subsequence

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
