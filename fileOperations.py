import numpy as np 

data= np.loadtxt('data.txt', delimiter=' ')
row_sums = np.sum(data, axis=1)
# print(row_sums)  # prints the sum of each row in the data.txt file.
# np.savetxt('output.txt',row_sums, fmt='%d')
output_data=np.column_stack((data,row_sums))
np.savetxt('output_and_sums.txt',output_data, fmt='%d',delimiter=' ')
print("Operation end !")
