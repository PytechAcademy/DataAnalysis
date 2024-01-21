import numpy as np
import time

# Create two large arrays
large_list1 = list(range(1000000))
large_list2 = list(range(1000000))
large_array1 = np.array(large_list1)
large_array2 = np.array(large_list2)

# Perform element-wise addition using Python lists
start_time = time.time()
result_list = [a + b for a, b in zip(large_list1, large_list2)]
end_time = time.time()
print(f"Python list addition took {end_time - start_time} seconds")

# Perform element-wise addition using NumPy arrays
start_time = time.time()
result_array = large_array1 + large_array2
end_time = time.time()
print(f"NumPy array addition took {end_time - start_time} seconds")