from numpy import *

# Create matrix
my_matrix = arange(20).reshape(5,4)
print (my_matrix)

# Concatenate arrays
array1 = array([1,3])
array2 = array([23,24,25])
array3 = array([8,4,3])

print(concatenate((array1, array2, array3)))

# Matrix multiplication (used a lot in games dev)
a1 = random.randn(5,5)
a2 = random.randn(5,5)

matrix1 = mat(a1)
matrix2 = mat(a2)

multMatrix = matrix1.T * matrix2.I
print (multMatrix)
