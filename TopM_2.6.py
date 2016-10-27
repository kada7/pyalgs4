#!/usr/bin/env python3
# encoding: utf-8

import operator
import sys
from functools import total_ordering

@total_ordering
class Transaction:
    def __init__(self, str):
        s = str.split()
        self.prod = s[0]
        self.date = s[1]
        self.price = float(s[2])

    def __eq__(self, other):
        return self.price == other.price

    def __lt__(self, other):
        return self.price < other.price

    def __str__(self):
        return "%-20s%11s%9.2f" % (self.prod, self.date, self.price)


class MinPQ:
    def __init__(self, maxN):
        self.pq = ['']
        self.maxN = maxN

    def isEmpty(self):
        return len(self.pq) == 1

    def size(self):
        return len(self.pq) - 1

    def insert(self, v):
        self.pq.append(v)
        self.swim(self.size())

    def delMin(self):
        min = self.pq[1]
        self.exch(1, self.size())
        self.pq.pop()
        self.sink(1)
        return min

    def more(self, i, j):
        return operator.gt(self.pq[i], self.pq[j])

    def swim(self, k):
        while k > 1 and self.more(int(k/2), k):
            self.exch(int(k/2), k)
            k = int(k/2)

    def sink(self,k):
        while 2*k <= self.size():
            j = int(2*k)
            if j < self.size() and self.more(j, j+1):
                j += 1
            if self.more(k, j) is False:
                break
            self.exch(k, j)
            k = j

    def exch(self, i, j):
        t = self.pq[i]
        self.pq[i] = self.pq[j]
        self.pq[j] = t

if __name__ == '__main__':
    M = int(sys.argv[1])
    file_path = sys.argv[2]

    pq = MinPQ(M)
    f = open(file_path, 'r')
    for line in f:
        trans = Transaction(line)
        pq.insert(trans)
        if pq.size() > M:
            pq.delMin()

    stack = []
    while pq.isEmpty() is False:
        stack.append(pq.delMin())

    for s in list(range(len(stack))):
        print(stack.pop())
