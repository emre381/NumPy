import numpy as np

arr=np.array([1,2,3,4,5])
print(arr)

#arr=np.arange(0,10,2)
#print(arr)

#arr=np.linspace(0,1,5)
#print(arr)

dimension = arr.ndim
data_type=arr.dtype
print("The Dimension Of array: ",dimension)
print("The Data Type Of array: ",data_type)