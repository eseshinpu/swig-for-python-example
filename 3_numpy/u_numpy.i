%module u_numpy
%include "std_string.i"

%{
#define SWIG_FILE_WITH_INIT
#include "u_numpy.h"
%}

%include "numpy.i"

%init %{
    import_array();
%}

%apply (double* IN_ARRAY1, int DIM1) {
    (double* seq, int n)
};

%apply (double* INPLACE_ARRAY1, int DIM1){
    (double* inp_seq, int n)
}

%include "u_numpy.h"