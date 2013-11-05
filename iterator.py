#!/usr/bin/env python


class BadIterator(object):
    def __init__(self, items):
        self.items = items
        self.index = 0

    def __iter__(self):
        return self

    def next(self):
        if self.index >= len(self.items):
            raise StopIteration
        else:
            ret = self.items[self.index]
            self.index += 1
            return ret



if __name__ == "__main__":
    bad = BadIterator([1,2,3,4,5,6,7,8])
    for b in bad:
        print b
