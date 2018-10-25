#include <stdio.h>

/*
* After playing around with this problem using containers and balls, 
* you realize that the rule, where n is the sum and k is number of terms.
*
* C is the number of different ways this can be arranged and follows:
*
*           | 1 if k == 1
* C(n, k) = |
*           | C(0, k - 1) + C(1, k - 1) + ... + C(n - 1, k - 1) + C(n, k - 1) if k > 1 
*
* Using recursion would result in exponential time complexity, therefore using 
* dynamic programming (memoization) is needed. Once a value is calculated it is saved
* in an array.
*/

#define SIZE 102

long int combinations[SIZE][SIZE];

int C(int n, int k) {
	int i, j;

	if (k == 1 || n == 0) {
		combinations[n][k] = 1;
		return combinations[n][k];
	}
	else if(combinations[n][k] != 0) {
		return combinations[n][k];
	}
	else {
		for (i = 0; i <= n; ++i) {
			combinations[n][k] = (combinations[n][k] + C(i, k - 1)) % 1000000;
		}

		return combinations[n][k];
	}
}

int main(void) {
	int i, j;
	for(i = 0; i < SIZE; ++i) {
		for(j = 0; j < SIZE; ++j) {
			combinations[i][j] = 0;
		}
	}

	int N, K;

	while(1) {
		scanf("%d %d", &N, &K);

		if (N == 0 && K == 0)
			break;

		printf("%d\n", C(N, K));
	}

	return 0;
}






