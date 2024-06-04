import numpy as np

arr = np.arange(10, 501, 1)
arr = np.power(arr, 2)
arr -= 234
print(arr.sum())
print(np.sum(arr))