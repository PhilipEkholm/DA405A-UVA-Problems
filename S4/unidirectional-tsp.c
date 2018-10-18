#include <stdio.h>

#define MAX_ROWS 102
#define MAX_COLS 102

int min(int a, int b) {
	return (a < b) ? a : b;
}

int max(int a, int b) {
	return (a < b) ? b : a;
}

int main(void) {
	int cols, rows, i, j;
	int field[MAX_ROWS][MAX_COLS], cost[MAX_ROWS][MAX_COLS];
	int route[MAX_ROWS][MAX_COLS];

	while (scanf("%d %d", &rows, &cols) != EOF) {

		for (i = 0; i < rows; ++i)
			for (j = 0; j < cols; j++)
				scanf("%d", &field[i][j]);

		for (i = 0; i < rows; ++i)
			cost[i][cols - 1] = field[i][cols - 1];

		for (j = cols - 2; j >= 0; --j)
			for (i = 0; i < rows; i++) {
				int up = i > 0 ? i - 1 : rows - 1;
				int mid = i;
				int down = i < rows - 1 ? i + 1 : 0;

				int a = min(up, min(mid, down));
				int c = max(up, max(mid, down));
				int b = up + mid + down - a - c;

				if (cost[a][j + 1] <= cost[b][j + 1] && cost[a][j + 1] <= cost[c][j + 1]) {
					route[i][j] = a;
					cost[i][j] = cost[a][j + 1] + field[i][j];
				} else if (cost[b][j + 1] <= cost[c][j + 1]) {
					route[i][j] = b;
					cost[i][j] = cost[b][j + 1] + field[i][j];
				} else {
					route[i][j] = c;
					cost[i][j] = cost[c][j + 1] + field[i][j];
				}
			}

		int bestRoute[MAX_COLS];

		bestRoute[0] = 0;
		for (i = 1; i < rows; ++i)
			if (cost[i][0] < cost[bestRoute[0]][0])
				bestRoute[0] = i;

		for (j = 1; j < cols; ++j)
			bestRoute[j] = route[bestRoute[j - 1]][j - 1];

		for (j = 0; j < cols - 1; ++j)
			printf("%d ", bestRoute[j] + 1);

		printf("%d\n", bestRoute[cols - 1] + 1);
		printf("%d\n", cost[bestRoute[0]][0]);

	}

	return 0;
}






