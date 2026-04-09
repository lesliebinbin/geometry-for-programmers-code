#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from IPython.core.formatters import BaseFormatter

ip = get_ipython()

if "text/org" not in ip.display_formatter.formatters:
    class OrgFormatter(BaseFormatter):
        format_type = "text/org"

        def pandas_to_org(self, df):
            from tabulate import tabulate
            # Removed index for a cleaner Org table, added headers
            return tabulate(df, headers="keys", tablefmt="orgtbl", showindex=False)

        def __call__(self, obj):
            # FIXED: Capital 'F' in DataFrame
            if isinstance(obj, pd.DataFrame):
                return self.pandas_to_org(obj)
            # Implicitly returns None for everything else (Matplotlib, Sympy, etc.)
            return None

    ip.display_formatter.formatters["text/org"] = OrgFormatter()


# In[ ]:


from sympy import *


# In[ ]:


a4, a3, a2, a1, a0 = symbols('a4 a3 a2 a1 a0')
z = symbols('z')


# In[ ]:


r = symbols('r')


# In[ ]:


formula = a4 * z ** 4 + a3 * z ** 3 + a2 * z ** 2 + a1 * z + a0  - r


# In[ ]:


zs = [0, 0.25, 0.5, 0.75, 1]
rs = [0.2, 0.4, 0.2, 0.8, 0]

equatations = [formula.subs({z: _z, r: _r}) for _z, _r in zip(zs, rs)]


# In[ ]:


equatations


# In[ ]:


equatations


# In[ ]:


solutions = solve(equatations, (a4, a3, a2, a1, a0))


# In[ ]:


solutions


# In[ ]:


formula_resolved = (formula + r).subs(solutions)


# In[ ]:


formula_resolved


# In[ ]:


import matplotlib.pyplot as plt
import numpy as np
z_scatter = [0, 0.25, 0.5, 0.75, 1]
r_scatter = np.array([formula_resolved.subs({z: z_val}) for z_val in zs])
z_plot = np.linspace(0, 1, 100)
r_plot = np.array([formula_resolved.subs({z: z_val}) for z_val in z_plot])


# In[ ]:

plt.scatter(z_scatter, r_scatter, color='blue')
plt.plot(z_plot, r_plot, color='red')
plt.show()

