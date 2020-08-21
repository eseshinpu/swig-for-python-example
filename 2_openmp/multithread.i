%module multithread
%include "std_string.i"

%{
#define SWIG_FILE_WITH_INIT
#include "multithread.h"
%}

%include "multithread.h"