#include <stdio.h>
#include <math.h>

/*
* "One could either do something the really hard way, or the simple way."
*                                                        - Philip Ekholm
*
* 1. Pick a point
* 2. Check against all other points and pick the point which is closest to the original
* 3. Repeat (1) for all points
*/

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

