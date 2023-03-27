import numpy as np

array = np.array([2.3, 0.1, -9.1, 2.4])
array = array.reshape(2,2)
array = array[0, 0:2]
print(array)
