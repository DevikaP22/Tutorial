import numpy as np
np.random.seed(0)
array1 = np.random.randint(0, 20, size=(3, 3))
array2 = np.random.randint(0, 20, size=(3, 3))

print("Array 1:")
print(array1)
print("\nArray 2:")
print(array2)
addition = array1 + array2
print("\nMatrix Addition:")
print(addition)
multiplication = np.matmul(array1, array2)
print("\nMatrix Multiplication:")
print(multiplication)
transpose = np.transpose(multiplication)
print("\nTranspose of the Product Matrix:")
print(transpose)
