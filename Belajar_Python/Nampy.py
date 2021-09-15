import numpy as np 

arr = np.array([1.2,3.2,3.4],ndmin=4)

newarr = arr.astype(int)
x = arr.copy()
y = arr.view()
print(y.base)
print(x.base)
arr[0] = 22
print(arr)
print(newarr)
print(newarr.dtype)

print(arr.shape)