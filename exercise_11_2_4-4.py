import numpy as np

import math


A = np.random.rand(5, 5)
print(A)

Ainv = np.linalg.inv(A)
print(Ainv)

I = A @ Ainv
I[np.isclose(I, 0)] = 0
print(I)