#include <stdio.h>
#include <math.h>

struct Point
{
    double x, y;
}point[10000];

double getEuclidDistance(struct Point p, struct Point q) {
    return sqrt((q.x - p.x)*(q.x - p.x) + (q.y - p.y)*(q.y - p.y));
}

int main(void)
{
    int numberOfSets, i, j;
    double d;

    while (scanf("%d", &numberOfSets) && numberOfSets) {
        for (i = 0; i < numberOfSets; ++i)
            scanf("%lf %lf", &point[i].x, &point[i].y);

        double min = 10000000;
        for (i = 0; i < numberOfSets - 1; ++i){
            for (j = i + 1; j < numberOfSets; ++j) {
                d = getEuclidDistance(point[i], point[j]);

                if (d < min) {
                    min = d;
                }
            }
        }

        if (min >= 10000)
            printf("INFINITY\n");
        else
            printf("%.4lf\n", min);
    }

    return 0;
}

