#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 09:48:43 2017

@author: xuchenwang
"""

# 4.1. Manually Consuming an Iterator
'''
You need to process items in an iterable, but for whatever reason, you can’t or don’t want to use a for loop.
'''


# 4.2. Delegating Iteration
'''
You have built a custom container object that internally holds a list, tuple, or some other 
iterable. You would like to make iteration work with your new container.
'''



# 4.3. Creating New Iteration Patterns with Generators
'''
You want to implement a custom iteration pattern that’s different than the usual built- in 
functions (e.g., range(), reversed(), etc.).
'''

def frange(start, stop, increment):
    while start<stop:
        yield start
        start += increment

# Use a for loop        
for n in frange(0,10,2):
    print(n)
# Use other function that consumes an iterable: list(), sum()
list(frange(0,10,2))    
# Use next()
r = frange(0,10,2)
next(r)
next(r)
next(r)
next(r)
next(r)
next(r) # StopIteration




# 4.4. Implementing the Iterator Protocol
'''
You are building custom objects on which you would like to support iteration, but would like 
an easy way to implement the iterator protocol.
'''

class Node(object):
    ''' Represent tree structures. '''
    def __init__(self,value):
        self._value = value
        self._children = []
        
    def __repr__(self):
        return 'Node({})'.format(self._value)
    
    def add_child(self,node):
        self._children.append(node)
    
    def __iter__(self):
        return iter(self._children)
    
    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()
    

if __name__ == '__main__': 
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for ch in root:
        print(ch)
    for ch in root.depth_first(): 
        print(ch)

    


# 4.5. Iterating in Reverse
'''
You want to iterate in reverse over a sequence.
'''

''' reversed works:
    the obj has a size that can be determined
    the obj implements a __reversed__ method '''

for x in reversed([1,2,3,4]):
    print(x)
    
f = open('somefile')
for line in reversed(list(f)):
    print(line, end='')

class Countdown(object):
    def __init__(self,start):
        self.start = start
    
    def __iter__(self):
        n = self.start
        while n>0:
            yield n
            n -= 1
            
    def __reversed__(self):
        n = 1
        while n<= self.start:
            yield n
            n += 1
        




# 4.6. Defining Generator Functions with Extra State
'''
You would like to define a generator function, but it involves extra state that you would 
like to expose to the user somehow.
'''

from collections import deque

class linehistory(object):
    def __init__(self,lines,histlen=3):
        self.lines = lines
        self.history = deque(maxlen=histlen)
        
    def __iter__(self):
        for lineno,line in enumerate(self.lines,1):
            self.history.append((lineno,line))
            yield line
            
    def clear(self):
        self.history.clear()
        
with open('somefile') as f:
    lines = linehistory(f)
    for line in lines:
        if 'python' in line:
            for lineno,hline in f.history:
                print('{}:{}'.format(lineno,hline), end='')
        





# 4.7. Taking a Slice of an Iterator
'''
You want to take a slice of data produced by an iterator, but the normal slicing operator doesn’t work.
'''

def count(n):
    while True:
        yield n
        n += 1
        
c = count(0)

import itertools
for x in itertools.islice(c,10,20):
    print(x)






# 4.8. Skipping the First Part of an Iterable
'''
You want to iterate over items in an iterable, but the first few items aren’t of interest 
and you just want to discard them.
'''

# skipping the first items according to a test function.
# dropwhile(function): drop the item as long as the function returns True
from itertools import dropwhile
with open('file') as f:
    for line in dropwhile(lambda line: line.startswith('#'),f):
        print(line,end='')
        
# know the exact number of items you want to skip
from itertools import islice
items = ['a', 'b', 'c', 1, 4, 10, 15]
for x in islice(items,3,None):
    print(x)
    




# 4.9. Iterating Over All Possible Combinations or Permutations
'''
You want to iterate over all of the possible combinations or permutations of a collection of items.
'''

items = ['a', 'b', 'c']

from itertools import permutations
for p in permutations(items):
    print(p)
for p in permutations(items,2):
    print(p)

from itertools import combinations
for p in combinations(items,2):
    print(p)
    
from itertools import combinations_with_replacement
for c in combinations_with_replacement(items,2):
    print(c)
    





# 4.10. Iterating Over the Index-Value Pairs of a Sequence
'''
You want to iterate over a sequence, but would like to keep track of which element 
of the sequence is currently being processed.
'''

word_summary = defaultdict(list)

with open('file') as f:
    lines = f.readlines()
    
for index,line in emumerate(lines,1):
    words = [c.strip().lower() for c in line.split()]
    for word in words:
        word_summary[word].append(index)
        
        
        
        
        
        
# 4.11. Iterating Over Multiple Sequences Simultaneously
'''
You want to iterate over the items contained in more than one sequence at a time.
'''

# zip() function: the length of the iteration is the same as the length of the shortest input.
from itertools import zip_longest

a = [1, 2, 3]
b = ['w', 'x', 'y', 'z']

list(zip(a,b))
dict(zip(a,b))

for x,y in zip_longest(a,b,fillvalue=0):
    print(x,y)
    






# 4.12. Iterating on Items in Separate Containers
'''
You need to perform the same operation on many objects, but the objects are contained in 
different containers, and you’d like to avoid nested loops without losing the readability 
of your code.
'''

from itertools import chain

a = [1, 2, 3, 4]
b = ['x', 'y', 'z']
for x in chain(a, b):
    print(x)






# 4.13. Creating Data Processing Pipelines
'''
You want to process data iteratively in the style of a data processing pipeline 
(similar to Unix pipes). For instance, you have a huge amount of data that needs 
to be processed, but it can’t fit entirely into memory.
'''







# 4.14. Flattening a Nested Sequence
'''
You have a nested sequence that you want to flatten into a single list of values.
'''

from collections import Iterable

def flatten(items, ignore_types=(str, bytes)):
    for item in items:
        if isinstance(item,Iterable) and not isinstance(item,ignore_types):
            yield from flatten(item)
        else:
            yield item
            
items = [1, 2, [3, 4, [5, 6], 7], 8]
list(flatten(items))






# 4.15. Iterating in Sorted Order Over Merged Sorted Iterables
'''
You have a collection of sorted sequences and you want to iterate over a sorted sequence of them 
all merged together.
'''

import heapq
a = [1, 4, 7, 10]
b = [2, 5, 6, 11]
for c in heapq.merge(a, b):    # a,b is sorted sequence
    print(c)







# 4.16. Replacing Infinite while Loops with an Iterator
'''
You have code that uses a while loop to iteratively process data because it involves 
a function or some kind of unusual test condition that doesn’t fall into the usual 
iteration pattern.
'''





    
    
    
    
    
    
    
    
    
    
    
    
    
    
