# PDQSort Python Extension

![PDQSort](pdqsort_logo.png)

## Introduction

PDQSort Python Extension is a C++ extension for Python that provides a fast sorting algorithm for various data types, including integers, floats, and strings. This extension is built upon the **PDQSort** algorithm, which is designed to be faster than traditional sorting algorithms like TimSort in many scenarios.

PDQSort Python Extension was inspired by the original PDQSort algorithm developed by Orson Peters. We'd like to extend immense credit and gratitude to Orson Peters for creating this efficient sorting algorithm.

## Disclaimer

This software is provided 'as-is,' without any express or implied warranty. The authors of the PDQSort Python Extension will not be held liable for any damages arising from the use of this software. Please use this software responsibly and be aware of the following conditions:

1. You must not misrepresent the origin of this software or claim that you wrote the original software.
2. Altered source versions must be clearly marked as such and must not be misrepresented as the original software.
3. This notice must not be removed or altered from any source distribution.

## Features

PDQSort Python Extension offers the following features:

- Sorting of integers, floats, strings, or mixed data types.
- Option to return the sorted data as a list of floats or strings.
- Compatibility with various Python versions.

## Drawbacks

As of the current version, there are some drawbacks to be aware of:

- PDQSort Python Extension may not always outperform Python's built-in TimSort algorithm for all data types. The choice of returning floats was made to speed up the results, but this may not be a fair comparison with TimSort if it were optimized similarly.  
- The extension has primarily been tested on a limited number of platforms, and its cross-platform compatibility may vary.

## Potential Use Cases

PDQSort Python Extension can be useful in scenarios where you need a fast sorting algorithm for data that doesn't necessarily require the original data types to be preserved. Some potential use cases include:

- Sorting large datasets efficiently.
- Implementing custom sorting logic for performance-critical applications.
- Research and experimentation with alternative sorting algorithms in Python.

## Future Directions

In future iterations, the PDQSort Python Extension may address some of its limitations, such as improving performance and handling additional data types. The extension's development is an ongoing process, and user feedback and contributions are welcome.

## Getting Started

To use PDQSort Python Extension, you need to install the module and import it into your Python scripts. Please refer to the documentation and usage examples provided in the project repository.

## Acknowledgments

- Orson Peters for creating the PDQSort algorithm.
- The Python community for their support and feedback.

# pdq4py

pdq4py is a Python C++ extension module that provides fast sorting capabilities for lists of integers, floats, and strings.

## Installation

Before using pdq4py, make sure you have the required dependencies installed:

1. [Python 3](https://www.python.org/downloads/): pdq4py is a Python C++ extension module, so you need Python 3 to use it.
2. [pybind11](https://pybind11.readthedocs.io/en/stable/): pdq4py utilizes pybind11 to create the Python C++ extension.
3. C++ Compiler: You'll also need a C++ compiler to compile the C++ code that powers the extension. Ensure you have a C++ compiler installed on your system.

   You can install pybind11 and its global development dependencies using pip3:

   ```bash
   pip3 install "pybind11[global]"
Building the Extension
Once you have installed pybind11, you can build the C++ extension for pdq4py using the following command:

bash
Copy code
python3 setup.py build_ext --inplace
This command will compile the C++ code and generate a shared library (.so file) in the current directory.

Usage
To use pdq4py, import it as a Python module in your Python scripts:

python
Copy code
import pdq4py

# Now you can use pdq4py's sorting functions
Example
Here's an example of how to use pdq4py to sort a list of numbers:

python
Copy code
import pdq4py

numbers = [4.5, 1.2, 3.7, 2.0, 6.1, 5.3]
sorted_numbers = pdq4py.pdqSort(numbers)
print(sorted_numbers)
Contributing
If you'd like to contribute to pdq4py or report issues, please visit the GitHub repository. We welcome contributions and feedback from the community.

## License

PDQSort Python Extension is open-source software released under the conditions described in the provided license.

For more information, please visit the project repository: [PDQSort Python Extension Repository](https://github.com/coryprimm/pdq4py)

**Thank you for using PDQSort Python Extension!**

*Cory Primm*

Similar Links:
The source:
https://github.com/orlp/pdqsort
Orson's walkthrough of the sorting algorithm:
https://www.youtube.com/watch?v=jz-PBiWwNjc

pdqSort implementations in straight python:
https://github.com/Chang-Chia-Chi/pdqsort

https://github.com/thatsOven/pdqsort-python
