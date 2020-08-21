"""
example using distutils

The great thing is that python provides a nice tool called distutils.
Let it do all the hard compiling work for you.
"""
from distutils.core import setup, Extension

module = Extension(name='_multithread',
                   sources=['multithread.cpp',
                            'multithread_wrap.cxx'],
                   extra_compile_args=["/openmp"],
                   )

setup(
    name='multithread',
    version="0.1",
    author="eseshinpu",
    description="""multithreading mothod""",
    ext_modules=[module],
    py_modules=['multithread'],
)
