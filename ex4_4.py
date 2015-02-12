# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# <markdowncell>

# ## probability density function

# <codecell>

def p(x):
    return 6 * x * (1 - x)

# <markdowncell>

# ## (A)

# <markdowncell>

# xs and ys

# <codecell>

dx = 0.001
xs = np.linspace(0, 1, 1/dx)
ys = p(xs)

# <codecell>

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_title("$6 \cdot x \cdot (1-x)$")
ax.set_xlabel("x")
ax.set_ylabel("p(x)")
ax.plot(xs, ys)

# <markdowncell>

# ## Approximating the Integral

# <codecell>

sum(dx * ys)

# <markdowncell>

# ## (B) Exact Integral

# <markdowncell>

# $$ \int_0^1 dx \cdot 6\cdot x \cdot (1-x)$$

# <markdowncell>

# $$ = 6 \int_0^1 dx\cdot(x - x^2) $$

# <markdowncell>

# $$ = 6\bigg[ \frac{x^2}{2} - \frac{x^3}{3}\bigg]_0^1 $$

# <markdowncell>

# $$ = 6 \bigg[\frac{1}{2} - \frac{1}{3}\bigg] $$

# <markdowncell>

# $$ = 1 $$

# <markdowncell>

# ## (C)

# <markdowncell>

# Yes, the integral of p over [0, 1] is 1

# <markdowncell>

# ## (D)

# <markdowncell>

# From the graph, the maximum value of p(x) is 1.5

