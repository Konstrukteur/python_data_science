import numpy as np
import matplotlib.pyplot as plt
from numpy.random import default_rng

rng = default_rng()
n_pts = 50
x = rng.standard_normal(n_pts)
print(x)