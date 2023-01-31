import numpy as np

import timeit

np.array([1, 2, 3])

a = np.array([1, 2, 3])
print(a)

r = range(17)
print(r)
print(list(r))

a = np.arange(17)
print(a)

print([3 * i for i in r])

print(3 * a)

print(a**2)

t1 = timeit.timeit("[i**2 for i in range(50)]")
t2 = timeit.timeit("import numpy as np; np.arange(50)**2")
print(t1, t2, t1/t1)