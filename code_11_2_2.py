import numpy as np

import timeit

a = np.array([[1, 2, 3], [4, 5, 6]])
print(a)

print(a.shape)

print(a[0, :])
print(a[:, 0])

A = a[0:2, 0:2]
print(A)

A = a[:2, :2]
print(A)

# inverse of a matrix
print("\n# inverse of a matrix")
Ainv = np.linalg.inv(A)
print(Ainv)

# adding and mulitplying matrices
print("\n# adding and mulitplying matrices")
print(A + Ainv)
print(A * Ainv)

# matrix mulitplication
print("\n# matrix mulitplication")
print(A @ Ainv)

# reshape()
print("\n# reshape()")
a = np.arange(16)
a.reshape((2, 8))
print(a)
b = a.reshape((4, 4))
print(b)

# reshape() using -1
print("\n# reshape() using -1")
print(a.reshape((-1, 2)))

# reshape() using -1 to create multidimensional array of one element arrays
print("\n# reshape() using -1 to create multidimensional array of one element arrays")
print(a.reshape((-1, 1)))
