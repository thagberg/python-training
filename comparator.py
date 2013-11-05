#!/usr/bin/env python

items = [4,2,3,7,8]
print items

new_items = sorted(items, cmp=lambda x,y: cmp(x, y))
print new_items

