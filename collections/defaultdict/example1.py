# Unlike dict, with defaultdict we do
# not need to check whether a key is present or not

from collections import defaultdict

colors = (
    ('nishan', 'red'),
    ('akib', 'blue'),
    ('tohfa', 'black'),
    ('nishan', 'white'),
    ('tohfa', 'red')
)

fav_colors = defaultdict(list)

for name, color in colors:
    fav_colors[name].append(color)

print(fav_colors)
