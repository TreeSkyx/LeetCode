"""
    705. Design HashSet
    Design a HashSet without using any built-in hash table libraries.

    Implement MyHashSet class:
    - void add(key) Inserts the value key into the HashSet.
    - bool contains(key) Returns whether the value key exists in the HashSet or not.
    - void remove(key) Removes the value key in the HashSet. If key does not exist in the HashSet, do nothing.
"""
class MyHashSet:

    def __init__(self):
        self.d = {}

    def add(self, key):
        self.d[key] = 1

    def remove(self, key):
        self.d[key] = 0

    def contains(self, key):
        return self.d.get(key,0)!=0