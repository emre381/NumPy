import numpy as np 
arr = np.array([10,20,30,40,50,60,70,80,90])
boolean_mask=arr>50
# print(arr[boolean_mask])  # Output: [60 70 80 90]
print(boolean_mask)
# choosen= arr[boolean_mask]
# print("more than 50 values:" , choosen)
boolean_mask=(arr > 30 )& (arr<70) & (arr>10)
print("between  30 and 70 values:", arr[boolean_mask])  