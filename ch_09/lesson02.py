# %%
from sympy import *
from sympy.vector import CoordSys3D

# %%
N = CoordSys3D("N")

# %%
a, b = 1 * N.i + 2 * N.j - 3 * N.k, 3 * N.i - 2 * N.j + N.k

# %%
a.cross(b)

# %%
a ^ b
