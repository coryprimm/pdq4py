from setuptools import setup, Extension, find_packages
from setuptools.command.build_ext import build_ext

# Define the Extension module
module = Extension('pdq4py', sources=['src/main.cpp'])

# Create a custom build_ext class to set the correct compiler options
class CustomBuildExt(build_ext):
    def build_extensions(self):
        for ext in self.extensions:
            ext.extra_compile_args = ['-std=c++14'] 
        super().build_extensions()
dependencies = [
    'pybind11[global]>=2.7'
]

setup(
    author='Cory Primm',
    author_email='corypr1mm@yahoo.com',
    name='pdq4py',
    version='1.0',
    ext_modules=[module],
    cmdclass={'build_ext': CustomBuildExt},
    packages=find_packages(),
    license='MIT',  
)
