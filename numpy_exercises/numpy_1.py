import numpy as np
# Creating a NumPy array from a Python list
my_list = [1, 2, 3, 4, 5]
my_array = np.array(my_list)
# Creating a NumPy array directly
my_array_direct = np.array([6, 7, 8, 9, 10])
# Adding two arrays element-wise
array1 = np.array([1, 2, 3])
array2 = np.array([4, 5, 6])
result = array1 + array2
print(result)  # Output: [5 7 9]
# Broadcasting a scalar to an array
array = np.array([1, 2, 3])
result = array + 5
print(result)  # Output: [6 7 8]
# Calculating mean, median, and standard deviation
data = np.array([10, 20, 30, 40, 50])
mean = np.mean(data)
median = np.median(data)
std_dev = np.std(data)
print(f"Mean: {mean}, Median: {median}, Standard Deviation: {std_dev}")