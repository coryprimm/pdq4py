cmake_minimum_required(VERSION 3.15...3.26)
project(pdq4py LANGUAGES CXX)

add_subdirectory(pybind11)

set(PYBIND11_FINDPYTHON ON)
find_package(pybind11 CONFIG REQUIRED)

pybind11_add_module(pdq4py MODULE src/main.cpp)

find_package(Python REQUIRED)

# Specify the output directory for shared libraries (".so" files)
set_target_properties(pdq4py PROPERTIES LIBRARY_OUTPUT_DIRECTORY ${CMAKE_BINARY_DIR})

# Link against the Python library
target_link_libraries(pdq4py PRIVATE Python::Python)
