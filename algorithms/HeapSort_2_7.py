#!/usr/bin/env python3
# encoding: utf-8

# Algorithms Edition 4th
# Page 323

import operator
import sys

def less(a, i, j):
    return operator.lt(a[i], a[j])

def sink(a, k, N):
    # N define the boundary of sinking
    while 2*k <= N:
        j = int(2*k)
        if j < N and less(a, j, j+1):
            j += 1
        if less(a, k, j) is False:
            break
        exch(a, k, j)
        k = j

def exch(a, i, j):
    t = a[i]
    a[i] = a[j]
    a[j] = t

def sort(a):
    N = len(a) - 1
    for k in list(range(1, int(N/2)+1))[::-1]:
        sink(a, k, N)
    while N > 1:
        exch(a, 1, N)
        N -= 1
        sink(a, 1, N)

if __name__ == '__main__':
    str = sys.argv[1]

    heap = ['']
    for s in list(str):
        heap.append(s)

    sort(heap)
    for i in heap:
        print(i, end='')
    print(end='\n')
