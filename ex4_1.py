# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# <markdowncell>

# ## Hair Eye Color

# <codecell>

hair_eye_color = pd.read_csv("data/HairEyeColor.csv", index_col=0)
hair_eye_color[:3]

# <markdowncell>

# ## Eye Hair Frequency

# <codecell>

eye_hair_freq = hair_eye_color.groupby(["Eye", "Hair"])["Freq"].sum()
eye_hair_freq[:3]

# <markdowncell>

# ## Eye Hair Marginal Proportions

# <codecell>

eye_hair_prop = eye_hair_freq/eye_hair_freq.sum()
np.round(eye_hair_prop, decimals=2)

# <markdowncell>

# ## Eye Frequency

# <codecell>

eye_freq = hair_eye_color.groupby("Eye")["Freq"].sum()
eye_freq

# <markdowncell>

# ## Eye Marginal Proportions

# <codecell>

eye_prop = eye_freq/eye_freq.sum()
np.round(eye_prop, decimals=2)

# <markdowncell>

# ## $ P(Hair^* | Blue Eyes) $

# <codecell>

eye_hair_prop["Blue"]/eye_prop["Blue"]

# <markdowncell>

# ## $ P(Hair^* | Brown Eyes)$

# <codecell>

eye_hair_prop["Brown"]/eye_prop["Brown"]

# <markdowncell>

# ## Hair Frequency

# <codecell>

hair_freq = hair_eye_color.groupby("Hair")["Freq"].sum()
hair_freq

# <markdowncell>

# ## Hair Marginal Proportions

# <codecell>

hair_prop = hair_freq/hair_freq.sum()
np.round(hair_prop, decimals=2)

# <markdowncell>

# ## $P(Eye^* | Brown Hair)$

# <codecell>

eye_hair_prop[:,"Brown"]/hair_prop["Brown"]

