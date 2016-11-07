#!/usr/bin/env python
# encoding: utf-8

# Algorithms 4th
# Page 379


class BinarySearchST:
    def __init__(self):
        self.keys = []
        self.vals = []

    def size(self):
        return len(self.keys)

    def get(self, key):
        if self.isEmpty():
            return None
        i = self.rank(key)
        if i < self.size() and self.keys[i] == key:
            return self.vals[i]
        else:
            return None

    def put(self, key, val):
        keys = self.keys
        vals = self.vals
        if not keys:
            keys.append(key)
            vals.append(val)
        else:
            i = self.rank(key)
            print('rank {}'.format(i))
            if i < self.size() and keys[i] == key:
                self.vals[i] = val
                return
            keys.insert(i, key)
            vals.insert(i, val)

    def rank(self, key):
        lo = 0
        hi = self.size() - 1
        while lo <= hi:
            mid = int(lo + (hi - lo) / 2)
            if key < self.keys[mid]:
                hi = mid - 1
            elif key > self.keys[mid]:
                lo = mid + 1
            else:
                return mid
        return lo

    def isEmpty(self):
        return len(self.keys) == 0
