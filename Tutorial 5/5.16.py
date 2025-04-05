import numpy as np

#create two numpy arrays of random integers between 0 and 20 of shape (3, 3)
np.random.seed(0)
array1 = np.random.randint(0, 20, size=(3, 3))
array2 = np.random.randint(0, 20, size=(3, 3))

print("Array 1:")
print(array1)
print("\nArray 2:")
print(array2)

#Perform matrix addition
addition = array1 + array2
print("\nMatrix Addition:")
print(addition)

#Perform matrix multiplication
multiplication = np.matmul(array1, array2)
print("\nMatrix Multiplication:")
print(multiplication)

#Perform transpose of the product matrix
transpose = np.transpose(multiplication)
print("\nTranspose of the Product Matrix:")
print(transpose)
