#!/usr/bin/env python

items = [1, 2, 3, 4, 5, 6]
print items

item_sum = reduce(lambda x, y: x + y, items)
print item_sum
