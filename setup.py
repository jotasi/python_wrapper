from distutils.core import setup
from Cython.Distutils import Extension
from Cython.Build import cythonize
import os

library_path = "../library"

ext = Extension(
    "py_sum",
    [os.path.join("src", "py_sum.pyx")],
    language = "c++",
    include_dirs = [os.path.join(library_path,"inc")],
    libraries = ["sum"],
    library_dirs = [os.path.join(library_path,"build")],
    cython_cplus = True,
    cython_c_in_temp = True
)

setup(
    name = "py_sum",
    ext_modules = cythonize(
        [ext],
        build_dir="build/cython",
        include_path=["src"]
    ),
)