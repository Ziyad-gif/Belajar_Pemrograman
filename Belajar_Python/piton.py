import numpy as np

arr= np.array([1,2,3,4,5])

x = arr[[True,False,True,False,True]]
filter = []
print(x)

for element in arr:
    if element >3:
        filter.append(True)

    else:
        filter.append(False)


newarr = arr[filter]
print(filter)
print(newarr)