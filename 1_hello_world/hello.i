%module hello
%include "std_string.i"

%{
#define SWIG_FILE_WITH_INIT
#include "hello.h"
%}

%include "hello.h"