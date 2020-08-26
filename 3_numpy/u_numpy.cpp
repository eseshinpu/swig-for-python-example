#include "u_numpy.h"

void notInplace(double *seq, int n)
{
    for (int i = 0; i < n; i++)
    {
        seq[i] = i;
    }
}

void inplace(double *inp_seq, int n)
{
    for (int i = 0; i < n; i++)
    {
        inp_seq[i] = i;
    }
}