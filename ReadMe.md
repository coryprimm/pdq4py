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

## License

PDQSort Python Extension is open-source software released under the conditions described in the provided license.

For more information, please visit the project repository: [PDQSort Python Extension Repository](https://github.com/coryprimm/pdq4py)

**Thank you for using PDQSort Python Extension!**

*Cory Primm*