#include <Python.h>
#include "pdqSort.h"
#include <vector>
#include <pybind11/pybind11.h>
#include <pybind11/stl.h>

namespace py = pybind11;

std::vector<py::object> pdq_sort(const std::vector<py::object>& input) {
    if (input.empty()) {
        PyErr_SetString(PyExc_ValueError, "Input vector is empty.");
        throw py::error_already_set();
    }
    const py::object& first_item = input[0];

    if (PyUnicode_Check(first_item.ptr())) {
        // First element is a string, sort and return strings
        std::vector<py::object> result_handles;
        std::vector<std::string> string_result;
        string_result.reserve(input.size());

        for (const py::object& item : input) {
            if (PyUnicode_Check(item.ptr())) {
                const char* str_value = PyUnicode_AsUTF8(item.ptr());
                if (str_value) {
                    string_result.emplace_back(str_value);
                } else {
                    PyErr_SetString(PyExc_TypeError, "Unable to convert Python string to C++ string.");
                    throw py::error_already_set();
                }
            } else {
                PyErr_SetString(PyExc_TypeError, "You cannot mix strings and other data types (ints floats objects etc) for this module ");
                throw py::error_already_set();
            }
        }

        pdqsort(string_result.begin(), string_result.end(), [](const std::string& a, const std::string& b) {
            return a < b;  
        });

        for (const std::string& str : string_result) {
            result_handles.push_back(py::str(str));
        }

        return result_handles;
    } else {
         std::vector<double> double_result;
        double_result.reserve(input.size());

        for (const py::object& item : input) {
            if (PyLong_Check(item.ptr())) {
                // Extract integer values
                double numeric_value = static_cast<double>(PyLong_AsLong(item.ptr()));
                double_result.push_back(numeric_value);
            } else if (PyFloat_Check(item.ptr())) {
                // Extract double values
                double numeric_value = PyFloat_AsDouble(item.ptr());
                double_result.push_back(numeric_value);
            } else {
                PyErr_SetString(PyExc_ValueError, "You have incomparable data types. pdq4py only currently supports lists of floats, integers, floats or lists of integers and floats. Objects are not supported, tuples aren't supported, and comparisons between strings and numeric types are not supported currently");
                throw py::error_already_set();
            }
        }
        pdqsort(double_result.begin(), double_result.end());

        std::vector<py::object> result_handles;
        result_handles.reserve(double_result.size());

        for (double value : double_result) {
            // Create Python float objects from double values
            result_handles.push_back(py::float_(value));
        }

        return result_handles;
        //Was 2 times as slow as python's built-in timsort, so abandoned:

        //Given numbers (ints or floats) this module will return an array of floats only

        //Can rewrite to return the correct data types but then because of casting issues becomes twice as slow as timsort :(

        // // First element is not a string, assume int or float, sort and return mixed objects
        // std::vector<py::object> mixed_result;

        // for (const py::object& item : input) {
        //     mixed_result.push_back(item);
        // }

        // pdqsort(mixed_result.begin(), mixed_result.end());

        // return mixed_result;
    }
}
PYBIND11_MODULE(pdq4py, m) {
    m.def("pdqSort", &pdq_sort, "Custom pdqsort function that takes a vector and returns a sorted vector.");
}






