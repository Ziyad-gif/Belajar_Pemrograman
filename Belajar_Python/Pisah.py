import numpy as np 

arr = np.array([1,2,3,4,5])

newarr = np.array_split(arr,4)
print(newarr[0])

arr2 = np.hsplit(arr,3)
print(arr2)

print(newarr)