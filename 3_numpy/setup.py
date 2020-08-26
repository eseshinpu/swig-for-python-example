"""
example using distutils

The great thing is that python provides a nice tool called distutils.
Let it do all the hard compiling work for you.
"""
from distutils.core import setup, Extension

import numpy as np

try:
    numpy_include = np.get_include()
except AttributeError:
    numpy_include = np.get_numpy_include()

module = Extension(name='_u_numpy',
                   sources=['u_numpy.cpp',
                            'u_numpy_wrap.cxx'],
                   include_dirs=[numpy_include],
                   )

setup(
    name='u_numpy',
    version="0.1",
    author="eseshinpu",
    description="""using numpy""",
    ext_modules=[module],
    py_modules=['u_numpy'],
)
