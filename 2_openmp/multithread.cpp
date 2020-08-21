#include "multithread.h"

void countNumber(int num)
{
    std::vector<int> array(num);
    for (int i = 0; i < num; i++)
    {
        array[i] = i * i;
    }
}

void countNumberUsingOpenmp(int num)
{
    std::vector<int> array(num);
#pragma omp parallel for schedule(dynamic)
    for (int i = 0; i < num; i++)
    {
        array[i] = i * i;
    }
}

void sleep(int num)
{
    for (int i = 0; i < num; i++)
    {
        Sleep(i * 1000);
    }
}

void sleepUsingOpenmp(int num)
{
#pragma omp parallel for schedule(dynamic)
    for (int i = 0; i < num; i++)
    {
        Sleep(i * 1000);
    }
}