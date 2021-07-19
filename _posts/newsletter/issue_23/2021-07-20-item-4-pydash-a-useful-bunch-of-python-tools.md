---
category: mlops
date: 2021-07-20 07:30:00
image: /assets/images/newsletter/issue_23/cesar-carlevarino-aragon-NL_DF0Klepc-unsplash.jpeg
important: This is a  handy bunch of tools
layout: post
link: https://pydash.readthedocs.io/en/latest/index.html
story_number: 4
title: 'Pydash: a useful bunch of Python tools'
word_count: 1,026
---

Some common tasks in python are harder than they need to be.

[Pydash](https://pydash.readthedocs.io/en/latest/index.html) is a nice library that attempt to plug some of those gaps

```python
import pydash

# Arrays
pydash.flatten([1, 2, [3, [4, 5, [6, 7]]]])
[1, 2, 3, [4, 5, [6, 7]]]

pydash.flatten_deep([1, 2, [3, [4, 5, [6, 7]]]])
[1, 2, 3, 4, 5, 6, 7]

# Collections
pydash.map_([{'name': 'moe', 'age': 40}, {'name': 'larry', 'age': 50}], 'name')
['moe', 'larry']

# Functions
curried = pydash.curry(lambda a, b, c: a + b + c)
curried(1, 2)(3)
```