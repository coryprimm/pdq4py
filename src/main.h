#ifndef MAIN_H
#define MAIN_H

#include <vector>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

// Declare the pdq_sort function
std::vector<py::handle> pdq_sort(const std::vector<py::handle>& input);

// Declare the Python module
PYBIND11_MODULE(pdq4py, m) {
    // Define the pdqSort function and add a docstring
    m.def("pdqSort", &pdq_sort, "Custom pdqsort function that takes a vector and returns a sorted vector.");
}

#endif  // MAIN_H
