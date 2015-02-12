# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import matplotlib.pyplot as plt
%matplotlib inline

# <codecell>

def normal(x, mu=0.0, sigma=1.0):
    return 1/(sigma * np.sqrt(2 * np.pi)) * np.exp(-0.5 * ((x-mu)/sigma) ** 2)

# <markdowncell>

# ## (A) Area under the curve

# <codecell>

mu = 0.0
sigma = 1.0
dx = 0.001
xs = np.linspace(mu - sigma, mu + sigma, 1/dx)
ys = normal(xs)
sum(ys * dx)

# <markdowncell>

# ## (B) 2/3 under the curve

# <markdowncell>

# 68% of probabilty mass lies between $\mu - \sigma$ and $\mu + \sigma$ which is roughly 2/3rds

# <markdowncell>

# In this case, $ \mu $ would be 162 cm with a $\sigma$ of 15

