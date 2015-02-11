# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

from ex2_1 import A, B, C, faces

# <codecell>

def rolls(faces, p, n=100):
    """Returns the expected number of rolls for each face given a list of faces
    and a probability function p, n is the number of rolls (default 100)"""
    return {x: int(p(x) * n) for x in faces}

# <markdowncell>

# 100 rolls of __A__

# <codecell>

rolls(faces, A)

# <markdowncell>

# 100 rolls of __B__

# <codecell>

rolls(faces, B)

# <markdowncell>

# 100 rolls of __C__

# <codecell>

rolls(faces, C)

# <markdowncell>

# The result, 1’s = 25, 2’s = 25, 3’s = 25, 4’s = 25, is closest to model __A__

# <markdowncell>

# The result, 1’s = 48, 2’s = 24, 3’s = 16, 4’s = 12, is closest to model __C__

