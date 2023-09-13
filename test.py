import pdq4py  # Import the module
import time
import random
import string 

#To test an array of floats and integers
random_mixed = [random.randint(1, 100) if random.choice([True, False]) else random.uniform(1.0, 100.0) for _ in range(10)]

# Generate a list of random letters to test strings
random_letters = [random.choice(string.ascii_letters) for _ in range(10)]


#To test integers:
random_integers = [random.randrange(0, 1000) for _ in range(10)] 

#To Test floats
random_floats = [random.uniform(0, 100) for _ in range(10)]

multipleTestsOf10 = [random_mixed, random_letters, random_integers, random_floats]

deep_copy_array = random_integers[:]

# randomArr = [random.uniform(0, 100) for _ in range(100)] # To create floats
def recordTime(function, arr, name):
	# Record the start time
	start_time = time.time()

	# Call your sorting function
	sorted_output = function(arr)

	# Record the end time
	end_time = time.time()

	# Calculate the elapsed time
	elapsed_time = end_time - start_time

	# Print the sorted output and the time taken
	# print("Sorted Output:", sorted_output)
	print("""Time Taken by {name}:""".format(name=name), elapsed_time, "seconds")
    # print("Sorted Output:", sorted_output)
	return [name,elapsed_time, sorted_output]

def builtInSort(arr):

    arr.sort()
    # print(arr)

    return arr

def pdqModuleSort(arr):

    newarr = pdq4py.pdqSort(arr)
    print(newarr)

    return newarr

for a in multipleTestsOf10:
     pdqModuleSort(a)


# modulePerformance = recordTime(pdqModuleSort, deep_copy_array, 'PDQ Module Performance')

# # print(random_mixed)

# builtInPerformance = recordTime(builtInSort, random_integers, 'Python\'s Built in Tim Sort')

# def comparePerformance(results):
#     # Sort the results by execution time (fastest to slowest)
#     sorted_results = sorted(results, key=lambda x: x[1])

#     # Print the sorted results
#     for i in range(len(sorted_results)):
#         name, elapsed_time, arr = sorted_results[i]
#         print(f"{name} was {i + 1} fastest in {elapsed_time:.10f} seconds")
# comparePerformance([modulePerformance, builtInPerformance])