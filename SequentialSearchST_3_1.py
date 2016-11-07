#!/usr/bin/env python3
# encoding: utf-8

# Algorithms Edition 4th
# Page 374

# Usage:
# Init the SequentialSearchST:
# > l = LinkList(Node('first key', 'first value'))
# > s = SequentialSearchST(l)
# > s.put('key', 'value')
# > s.get('key')
# > 'value'

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next= None


class LinkList:
    def __init__(self,node):
        self.head = node
        self.head.next = None
        self.tail = self.head

    def add(self, node):
        self.tail.next = node
        self.tail = self.tail.next


class SequentialSearchST:
    def __init__(self, link_list):
        self.link_list = link_list

    def get(self, key):
        x = self.link_list.head
        while x is not None:
            if x.key == key:
                return x.val
            else:
                x = x.next
        return None

    def put(self, key, val):
        x = self.link_list.head
        while x is not None:
            if x.key == key:
                x.val = val
                return
            else:
                x = x.next
        self.link_list.add(Node(key, val))
