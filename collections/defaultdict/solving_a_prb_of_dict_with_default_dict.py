#  ======================================= Problem =========================================

"""
1)

some_dict = {
    'colors': {
        'favorite': ''
    }
}

some_dict['colors']['favorite'] = "Yellow"

print(some_dict)

==============================================================================================

This piece of code works like a charm, but if we don't have the key "favorite" and "colors" already in the
"some_dict" dictionary then it will raise a key error! See bellow example!

==============================================================================================

2)

some_dict = {}

some_dict['colors']['favorite'] = "Yellow"

print(some_dict)

"""

# ================================== Solution With defaultdict =================================

from collections import defaultdict
import json

tree = lambda: defaultdict(tree)
some_dict = tree()

some_dict['colors']['favorite'] = 'yellow'

print(json.dumps(some_dict))
