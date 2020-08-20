"""
example using distutils

The great thing is that python provides a nice tool called distutils.
Let it do all the hard compiling work for you.
"""
from distutils.core import setup, Extension

module = Extension(name='_hello',
                   sources=['hello.cpp',
                            'hello_wrap.cxx'],
                   )

setup(
    name='hello',
    version="0.1",
    author="eseshinpu",
    description="""hello world""",
    ext_modules=[module],
    py_modules=['hello'],
)
