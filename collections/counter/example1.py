from collections import Counter

colors = (
    ('nishan', 'red'),
    ('akib', 'blue'),
    ('tohfa', 'black'),
    ('nishan', 'white'),
    ('tohfa', 'red')
)

favs = Counter(name for name, color in colors)

print(favs)


#  ===================================== Line counter =============================

"""

with open('filename', 'rb') as f:
    line_count = Counter(f)
print(line_count)

"""

