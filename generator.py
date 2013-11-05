#!/usr/bin/env python

class BadGenerator(object):
    def __init__(self):
        self.count = 0

    def __iter__(self):
        return self

    def next(self):
        if self.count > 10:
            raise StopIteration
        self.count += 1
        yield self.count


if __name__ == "__main__":
    bad = BadGenerator()
    for b in bad:
        print b
