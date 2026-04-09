# %%
from sympy import *

# %%
z1, z2, z3, z4, a, b, c, d = symbols("z1 z2 z3 z4 a b c d")
z, x = symbols("z x")
formula = a * (x**3) + b * (x**2) + c * x + d - z

# %%
systems = [
    formula.subs({x: 0, z: z1}),
    formula.subs({x: 1 / 3, z: z2}),
    formula.subs({x: 2 / 3, z: z3}),
    formula.subs({x: 1, z: z4}),
]

# %% 
systems

# %%
solve(systems, (a, b, c, d))
