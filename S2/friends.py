import sys
from collections import Counter

# The key to solve the problem is using a disjointed set data-structure.
# 
# 1. Create a disjointed set for every person in the town
# 2. Read a line containing information about who is a friend with who
# 2. If a person A is friend with person B, unionize these two (union(A, B))
# 3. Repeat (2) until you've read all relations
# 4. Find the biggest unioned set. This will be the mode number in the DS-structure
#    (the most common number in the array)

class UnionFind:
    def __init__(self, n):
        self._id = list(range(n))
        self._sz = [1] * n

    def _root(self, i):
        j = i
        while (j != self._id[j]):
            self._id[j] = self._id[self._id[j]]
            j = self._id[j]
        return j

    def find(self, p, q):
        return self._root(p) == self._root(q)

    def union(self, p, q):
        i = self._root(p)
        j = self._root(q)
        if i == j:
            return
        if (self._sz[i] < self._sz[j]):
            self._id[i] = j
            self._sz[j] += self._sz[i]
        else:
            self._id[j] = i
            self._sz[i] += self._sz[j]


testCases = int(sys.stdin.readline())

for i in range(0, testCases):
    N, M = [int(s) for s in sys.stdin.readline().split()]
    uf = UnionFind(N + 1)

    for j in range(0, M):
        A, B = [int(s) for s in sys.stdin.readline().split()]
        uf.union(A, B)

    print(max(uf._sz))








