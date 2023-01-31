import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng

rng = default_rng()
n_pts = 50
x = rng.standard_normal(n_pts)
print(x)

y = 5*x + rng.standard_normal(n_pts)

fig, ax = plt.subplots()
ax.scatter(x, y)
plt.show()