import numpy as np

arr1 = np.array([[1,2,3],[1,2,3]])
arr2 = np.array([[1,2,3],[1,23,4]])

arr3 = np.concatenate((arr1,arr2),axis=1)
arr = np.dstack((arr1,arr2))

print(arr3)

print(arr)