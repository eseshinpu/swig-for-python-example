#include "multithread.h"

void countNumber(int num)
{
    for (int i = 0; i < num; i++)
    {
        printf("%d\n", i);
    }
}

void countNumberUsingOpenmp(int num)
{
#pragma omp parallel
    {
#pragma omp for nowait
        for (int i = 0; i < num; i++)
        {
            printf("%d\n", i);
        }
    }
}