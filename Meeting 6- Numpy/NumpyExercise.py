import numpy as np #Importing the Numpy library so that it can be used
a = np.array([1,2,3,4,5]) # Create a 1D Numpy array
b = np.array([6,7,8,9,10])# Create a 1D Numpy array
c = np.array(["programming", 36, 36.9]) #Create 1D Numpy array with string, integer and float
# Array2D = np.array([[1,2,3,4,5], [6,7,8,9,10], [11,12,13,14,15]])#Create 2D array
array3D = np.array([[[1,2,3], [4,5,6]],
[[7,8,9], [10,11,12]],
[[13,14,15], [16,17,18]]]) #Create 3D array

data = np.array([[1,2,3,4], [5,6,7,8]])
# print(data.shape) #output (2,4) because have 2 rows, 4 columns
# print(data[0, 3]) #output 4 because (Y,X)
# print (data[1,2]) #print output 7 (challenge)
print(a) # Displays the output of the Numpy array that has been created
print(b) # Displays the output of the Numpy array that has been created
# print(c)
#print(Array2D)
print(array3D)
# print(data[:, 2]) #(rows,column) (all rows, index 2 column) output is [3 7]
# print(data[1, :]) #(index 1 row, all columns) output is [ 5 6 7 8]
# print(data[:, 1:3]) #output is [[2 3][6 7]] (all rows, column index 1 until before 3 (1-2))
# print(data[1, 1:4]) #ouput is [6 7 8] (rows index 1,column index 1 until before 4 (1-3) )
# print(data[:,1:4]) #challenge print [[2 3 4][6 7 8]]
# print(data.diagonal(2)) #ouput is [3 8] diagonal from column index 2
# print(data.diagonal(3)) #ouput is [4]

# empty = np.zeros((4,4), dtype="int")
# # print(empty)

# empty[0, 1:4] = [1,55,3] #change number column index 1-3
# # print(empty)

# empty[-1, 0] = 7 #-1 = row index terakhir, change the last row index
# empty[1:3, 1] = [9,5] #change the row index 1-2, column index 1
# empty[2:4, 2:4] = [[0,70],[14,22]] #challenge fill the number in right bottom corner
# print(empty) # ^ 
#              # | new value