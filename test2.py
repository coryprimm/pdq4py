import pdq4py  # Import the module
import time
import random
import string
import copy
import matplotlib.pyplot as plt

def generate_random_floats(n):
    return [random.uniform(0, 1000) for _ in range(n)]

def generate_random_integers(n):
     return [random.randrange(0, 1000) for _ in range(n)]

def generate_random_letters(n):
    return [random.choice(string.ascii_letters) for _ in range(n)]

def generate_random_mixed(n):
    return [random.randint(1, 100) if random.choice([True, False]) else random.uniform(1.0, 100.0) for _ in range(n)]

def record_time(function, arr):
    start_time = time.time()
    sorted_output = function(arr)
    end_time = time.time()
    elapsed_time = end_time - start_time
    return elapsed_time

def compare_performance(sort_functions, array_sizes):
    performance_data = {str(sort_function.__name__): [] for sort_function in sort_functions}
    
    for size in array_sizes:
        arr = generate_random_letters(size)
        deep_copy_array = copy.deepcopy(arr)

        for sort_function in sort_functions:
            elapsed_time = record_time(sort_function, deep_copy_array)
            performance_data[str(sort_function.__name__)].append((size, elapsed_time))

    return performance_data

if __name__ == "__main__":
    array_sizes = [10, 100, 1000, 10000, 100000, 1000000]  # Adjust as needed
    sort_functions = [sorted, pdq4py.pdqSort]  # Add more sorting functions if necessary

    performance_data = compare_performance(sort_functions, array_sizes)

    # Create a performance comparison graph
    for sort_function, data in performance_data.items():
        x, y = zip(*data)
        plt.plot(x, y, label=sort_function)

    plt.xlabel("Number of Elements")
    plt.ylabel("Time (seconds)")
    plt.title("Performance Comparison of Mixed Arrays (Ints and Floats)")
    plt.legend()
    plt.show()
     # Add an event handler to close the figure when a key is pressed
    plt.connect('key_press_event', lambda event: plt.close())

    plt.show()

