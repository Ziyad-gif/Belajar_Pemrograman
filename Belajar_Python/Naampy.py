import numpy as np 

arr = np.array([[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]])

newarr = arr.reshape(4,4)

print(newarr)

for x in arr:
    for y in x:

        for z in y:
            print(z)
