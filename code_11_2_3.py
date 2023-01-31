import numpy as np

import math


# e
print("# e")
print(math.e)
print(np.e)
print(math.e == np.e)

# pi
print("\n# pi")
print(np.pi)
# print(np.tau)

print(math.tau == 2 * np.pi)

# trigonometric functions
print("\n# trigonometric functions")
print(np.cos(math.tau))
print(np.sin(math.tau))
print(np.log(np.e))
print(np.log10(np.e))

# vectorized operations
print("\n# vectorized operations")
print(np.arange(5))
angles = math.tau * np.arange(5) / 4
print(angles)

# print(math.cos(angles))
a = np.cos(angles)
print(a)

# isclose()
print("\n# isclose()")
print(np.isclose(0.01, 0))
print(np.isclose(10**(-16), 0))
print(np.isclose(a, 0))

print(a[np.isclose(a, 0)])
a[np.isclose(a, 0)] = 0
print(a)

# linspace()
print("\n# linspace()")
angles = np.linspace(0, math.tau, 5)
print(angles)

a = np.cos(angles)
a[np.isclose(a, 0)] = 0
print(a)

angles = np.linspace(0, math.tau, 100)
print(angles)
print(np.cos(angles))
