from distutils.core import setup, Extension

module = Extension(name='_hello',  # extension full name
                   sources=['./c_ext/hello.cpp',
                            './c_ext/hello_wrap.cxx'],
                   )

setup(
    name='hello',
    version="0.1",
    author="eseshinpu",
    description="""hello world""",
    ext_modules=[module],
    py_modules=['hello'],
)
