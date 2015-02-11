# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

faces = [1, 2, 3, 4]

# <markdowncell>

# ## Model A 
# 
# $ p(x) = \frac{1}{4} $

# <codecell>

def A(x):
    return 1/4.0

# <markdowncell>

# ## Model B
# 
# $ p(x) = \frac{x}{10} $

# <codecell>

def B(x):
    return x/10.0

# <markdowncell>

# ## Model C
# 
# $ p(x) = \frac{12}{25\cdot x} $

# <codecell>

def C(x):
    return 12/(25.0 * x)

# <markdowncell>

# ## Evaulating Models

# <markdowncell>

# * Model A

# <codecell>

[A(x) for x in faces]

# <markdowncell>

# Model A is an unbiased model, with equal probabilities for each face

# <markdowncell>

# * Model B

# <codecell>

[B(x) for x in faces]

# <markdowncell>

# Model B is biased proportional to the value of each face

# <markdowncell>

# * Model C

# <codecell>

[C(x) for x in faces]

# <markdowncell>

# Model C is is biased inversely proportional to the value of each face

