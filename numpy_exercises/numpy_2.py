import sys
import numpy as np

# Creating a Python list with 1 million integers
python_list = list(range(1000000))
# Creating a NumPy array with the same data
numpy_array = np.array(python_list)
# Check memory usage in bytes
python_list_memory = sys.getsizeof(python_list)
numpy_array_memory = numpy_array.nbytes
print(f"Memory usage of Python list: {python_list_memory} bytes")
print(f"Memory usage of NumPy array: {numpy_array_memory} bytes")