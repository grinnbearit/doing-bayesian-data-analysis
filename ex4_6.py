# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import numpy as np
import pandas as pd
from pandas import Series, DataFrame

# <markdowncell>

# ## $ P(grade) $

# <codecell>

p_grade = Series([0.2, 0.2, 0.6], index=["first", "sixth", "eleventh"])
p_grade

# <markdowncell>

# ## $ P(food | grade) $

# <codecell>

p_food_1_grade = Series([0.3, 0.6, 0.1,
                         0.6, 0.3, 0.1,
                         0.3, 0.1, 0.6],
                         index=pd.MultiIndex(levels=[["first", "sixth", "eleventh"],
                                                     ["ice cream", "fruit", "french fries"]],
                                             labels=[[0]*3 + [1]*3 + [2]*3,
                                                     [0, 1, 2]*3],
                                             names=["grade", "food"]))
p_food_1_grade

# <markdowncell>

# ## $ P(grade, food) $

# <codecell>

p_grade_food = p_food_1_grade.multiply(p_grade, level=0)
p_grade_food

# <markdowncell>

# ## Checking Independence

# <markdowncell>

# $ P(grade) $ and $ P(food) $ are independent if $ P(grade, food) = P(grade) \cdot P(food) $

# <markdowncell>

# ### $ P(grade) $

# <codecell>

p_grade = p_grade_food.sum(level=0)
p_grade

# <markdowncell>

# ### $ P(food) $

# <codecell>

p_food = p_grade_food.sum(level=1)
p_food

# <markdowncell>

# ### $ P(grade) \cdot P(food) $

# <codecell>

probabilities = []
for grade in p_grade:
    for food in p_food:
        probabilities.append(grade * food)
        
Series(probabilities, index=p_grade_food.index)

# <markdowncell>

# Since this is not equal to $ P(grade, food) $, the events are not independent

