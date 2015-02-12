# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# <codecell>

N = 500
p_heads = 0.8

# <markdowncell>

# Generating a random sample of N flips

# <codecell>

flip_sequence = np.random.choice([0.0, 1.0], p=[1-p_heads, p_heads], size=N, replace=True)
flip_sequence[:5]

# <codecell>

r = np.cumsum(flip_sequence)
n = np.arange(1, N+1)
run_prop = r/n
run_prop[:5]

# <codecell>

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
ax.set_title("Running Proportion of Heads")
ax.set_xscale("log")
ax.set_xlabel("Flip Number")
ax.set_ylabel("Proportion of Heads")
ax.plot(n, run_prop, "bo")
xlim = ax.get_xlim()[1]
ax.plot([0, xlim], [p_heads, p_heads],"k--")

