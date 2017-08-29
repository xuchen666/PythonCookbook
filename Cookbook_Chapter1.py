#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 12:12:19 2017

@author: xuchenwang
"""

# 1.1 Unpacking a sequence into separate variables
'''
You have an N-element tuple or sequence that you would like to unpack into 
a collection of N variables.
'''

data = ['abc', 1, (1,4,5)]

string,number,array = data
string,number,(a,b,c) = data
_,number,(a,_,c) = data     # Discard certain values.



# 1.2 Unpacking elements from iterables of arbitrary length
'''
You need to unpack N elements from an iterable, but the iterable may be longer than 
N elements, causing a “too many values to unpack” exception.
'''

string,*num = data    # *variable returns a list.



# 1.3 Keeping the last N items
'''
You want to keep a limited history of the last few items seen during iteration 
or during some other kind of processing.
'''

from collections import deque

'''
q = deque(maxlen=3)
q.append(1)
q.appendleft(4)
q.pop()
q.popleft()
'''


def search(lines,pattern,history=5):
    '''This is a generator function.
    '''
    previous_lines = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line,previous_lines
        previous_lines.append(line)
        



# 1.4 Finding the largest or smallest N items
'''
You want to make a list of the largest or smallest N items in a collection.
'''

import heapq

nums = [2,4,56,34,6,323,98,45]
print(heapq.nlargest(3, nums))
print(heapq.nsmallest(3, nums))

'''
heapq.heappush(nums,value)   # put the smallest value in the first place
heapq.heappop(nums)          # pop the first element and returns it
heapq.heapify(nums)
'''



# 1.5 Implementing a priority queue
'''
You want to implement a queue that sorts items by a given priority and always returns 
the item with the highest priority on each pop operation.
'''

class PriorityQueue(object):
    '''Represents a queue with the highest priority in the first element'''
    def __init__(self):
        self.queue = []
        self.index = 0
        
    def __str__(self):
        q = []
        for item in self.queue:
            q.append(str(item))
        return '\n'.join(q)
        
    def push(self,priority,item):
        heapq.heappush(self.queue,(-priority,self.index,item))
        self.index += 1
        
    def pop(self):
        return heapq.heappop(self.queue)[2]
    
    
q = PriorityQueue()
q.push(1,'apple')
q.push(4,'pear')
q.push(5,'peach')
q.push(1,'orange')
q.pop()



# 1.6 Mapping keys to multiple values in a dictionary
'''
You want to make a dictionary that maps keys to more than one value (a so-called “multidict”).                          
'''

from collections import defaultdict

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(5)

d = defaultdict(set)
d['a'].add(1)

d = {}
d.setdefault('a',[]).append(1)



# 1.7 Keeping dictionaries in order
'''
You want to create a dictionary, and you also want to control the order of items when 
iterating or serializing.
'''

from collections import OrderDict

d = OrderDict()   # The size is twice as the normal dict.




# 1.8 Calculating with Dictionaries
'''
You want to perform various calculations (e.g., minimum value, maximum value, 
sorting, etc.) on a dictionary of data.
'''

prices = {
       'ACME': 45.23,
       'AAPL': 612.78,
       'IBM': 205.55,
       'HPQ': 37.20,
       'FB': 10.75
}

min_price = min(zip(prices.values(),prices.keys()))
max_price = max(zip(prices.values(),prices.keys()))
max_sorted = sorted(zip(prices.values(),prices.keys()))

'''
zip() creates an iterator that can only be consumed once. 
prices_and_names = zip(prices.values(), prices.keys()) 
print(min(prices_and_names)) # OK
print(max(prices_and_names)) # ValueError: max() arg is an empty sequence
'''

'''
min(prices)             # get the min key
min(prices.values())    # get the min value (without the corresponding key)

min(prices, key=lambda k: prices[k])             # get the key for the min value
prices[min(prices, key=lambda k: prices[k])]     # get the min value
'''



# 1.9 Finding commonalities in two dictionaries
'''
You have two dictionaries and want to find out what they might have in common 
(same keys, same values, etc.).
'''

'''
set operators: & | -
keys, items
'''

a={
'x' : 1,
'y' : 2,
'z' : 3 }

b={
'w' : 10,
'x' : 11,
'y' : 2 }

a.keys() &  b.keys()




# 1.10 Removing duplicates from sequence while maintaining order
'''
You want to eliminate the duplicate values in a sequence, but preserve the order 
of the remaining items.
'''

# For hashable object: List
def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)
            
a = [1, 5, 2, 1, 9, 1, 5, 10]
list(dedupe(a))

# Work for both hashable and unhashable types
def dedupe(items,key=None):
    '''
    1. Items is a sequence of dict. Key is a function which returns values of keys.
    2. Items is a sequence. Key is None.
    '''
    seen = set()
    for item in items:
        value = item if key is None else key(item)
        if value not in seen:
            yield item
            seen.add(value)

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]
list(dedupe(a,key=lambda d: (d['x'],d['y'])))



# 1.11 Naming a slice
'''
Your program has become an unreadable mess of hardcoded slice indices and you want 
to clean it up.
'''

'''
a = slice(5,15,2)
a.start
a.stop
a.step

a.indices(8)
'''

record = '....................100          .......513.25     ..........'

SHARES = slice(20,32)
PRICE  = slice(40,48)
    
cost = int(record[SHARES]) * float(record[PRICE])



# 1.12 Determining the most frequently occuring items in a sequence
'''
You have a sequence of items, and you’d like to determine the most frequently 
occurring items in the sequence.
'''

words = [
       'look', 'into', 'my', 'eyes', 'look', 'into', 'my', 'eyes',
       'the', 'eyes', 'the', 'eyes', 'the', 'eyes', 'not', 'around', 'the',
       'eyes', "don't", 'look', 'around', 'the', 'eyes', 'look', 'into',
       'my', 'eyes', "you're", 'under'
]

from collections import Counter  

word_counts = Counter(words)      # returns a dict of frequency
'''
Counter({'around': 2,
         "don't": 1,
         'eyes': 8,
         'into': 3,
         'look': 4,
         'my': 3,
         'not': 1,
         'the': 5,
         'under': 1,
         "you're": 1})
'''

top_three = word_counts.most_common(3)

morewords = ['why','are','you','not','looking','in','my','eyes']
word_counts.update(morewords)




# 1.13 Sorting a list of dictionaries by a common key
'''
You have a list of dictionaries and you would like to sort the entries according 
to one or more of the dictionary values.
'''

rows = [
        {'fname': 'Brian', 'lname': 'Jones', 'uid': 1003},
        {'fname': 'David', 'lname': 'Beazley', 'uid': 1002},
        {'fname': 'John', 'lname': 'Cleese', 'uid': 1001},
        {'fname': 'Big', 'lname': 'Jones', 'uid': 1004}
]

from operator import itemgetter

sort_by_fname = sorted(rows, key=lambda r: r['fname'])
sort_by_fname_uid = sorted(rows, key=lambda r: (r['fname'],r['uid']))

'''
itemgetter() returns a callable object(a bit faster):
itemgetter('fname')(rows[1])
'''
sort_by_fname_ = sorted(rows, key=itemgetter('fname'))
sort_by_fname_uid_ = sorted(rows, key=itemgetter('fname','uid'))




# 1.14 Sorting objects without native comparison support
'''
You want to sort objects of the same class, but they don’t natively support comparison operations.
'''

class User(object):
    def __init__(self,user_id):
        self.user_id = user_id
        
    def __repr__(self):
        return 'User %d'%self.user_id

    
users = [User(23), User(3), User(99)]


sorted(users, key=lambda u: u.user_id)  

from operator import attrgetter
sorted(users, key=attrgetter('user_id'))




# 1.15 Grouping records together based on a field
'''
You have a sequence of dictionaries or instances and you want to iterate over the data 
in groups based on the value of a particular field, such as date.
'''

rows = [
        {'address': '5412 N CLARK', 'date': '07/01/2012'},
        {'address': '5148 N CLARK', 'date': '07/04/2012'},
        {'address': '5800 E 58TH', 'date': '07/02/2012'},
        {'address': '2122 N CLARK', 'date': '07/03/2012'},
        {'address': '5645 N RAVENSWOOD', 'date': '07/02/2012'},
        {'address': '1060 W ADDISON', 'date': '07/02/2012'},
        {'address': '4801 N BROADWAY', 'date': '07/01/2012'},
        {'address': '1039 W GRANVILLE', 'date': '07/04/2012'},
]


from operator import itemgetter
from itertools import groupby

# Sort by the desired field first
rows.sort(key=itemgetter('date'))

# Iterate in groups
for date,items in groupby(rows,key=itemgetter('date')):
    print(date)
    for i in items:
        print('    ',i)
        

'''
If memory is no concern, it may be faster to do this than to first sort the records and 
iterate using groupby().
'''
from collections import defaultdict

rows_by_date = defaultdict(list)
for row in rows:
    rows_by_date[row['date']].append(row)
        
    
    
    
# 1.16 Filtering the sequence element
'''
You have data inside of a sequence, and need to extract values or reduce the sequence using some criteria.
'''

# Use list comprehension or generator
mylist = [1, 4, -5, 10, -7, 2, 3, -1]
[n for n in mylist if n>0]
[n if n>0 else 0 for n in mylist]

# Make a function first and use filter() for a complicated situation
vals = ['1', '2', '-3', '-', '4', 'N/A', '5']

def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False
    
ivals = filter(is_int,vals)   # returns an iterator, use list().
list(ivals)    

# Use itertools.compress(), it returns an iterator
from itertools import compress
addresses = [
        '5412 N CLARK',
        '5148 N CLARK',
        '5800 E 58TH',
        '2122 N CLARK'
        '5645 N RAVENSWOOD',
        '1060 W ADDISON',
        '4801 N BROADWAY',
        '1039 W GRANVILLE',
    ]
counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

more5 = [n>5 for n in counts]
list(compress(addresses,more5))




# 1.17 Extracting a subsequence of a dictionary
'''
You want to make a dictionary that is a subset of another dictionary. (Simply use dictionary comprehension)
'''

prices = {
       'ACME': 45.23,
       'AAPL': 612.78,
       'IBM': 205.55,
       'HPQ': 37.20,
       'FB': 10.75
}

p1 = {key:value for key,value in prices.items() if value>40}

tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = {key:value for key,value in prices.items() if key in tech_names}




# 1.18 Mapping names to sequence elements
'''
You have code that accesses list or tuple elements by position, but this makes the code 
somewhat difficult to read at times. You’d also like to be less dependent on position 
in the structure, by accessing the elements by name.
'''

from collections import namedtuple
Stock = namedtuple('Stock',['name','share','price'])
s = Stock('AMC',10,9)
s = s._replace(share=75)

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])
stock_prototype = Stock('', 0, 0.0, None, None)

def dict_to_stock(s):
    return stock_prototype._replace(**s)

dict_to_stock({'name': 'ACME', 'shares': 100, 'price': 123.45})




# 1.19 Transforming and reducing data at the same time
'''
You need to execute a reduction function (e.g., sum(), min(), max()), 
but first need to transform or filter the data.
Use generator expression.
'''

portfolio = [
       {'name':'GOOG', 'shares': 50},
       {'name':'YHOO', 'shares': 75},
       {'name':'AOL', 'shares': 20},
       {'name':'SCOX', 'shares': 65}
    ]

min_shares = min(s['shares'] for s in portfolio)
min_shares = min(portfolio,key=lambda s:s['shares'])




# 1.20 Combining multiple mapings into a single mapping
'''
You have multiple dictionaries or mappings that you want to logically combine 
into a single mapping to perform certain operations, such as looking up values 
or checking for the existence of keys.
'''

from collections import ChainMap

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

c = ChainMap(a,b)    # only affects the first element


values = ChainMap()
values['x'] = 1

values = values.new_child()  # Adding a new mapping
values['x'] = 2
values = values.new_child()
values['x'] = 3

values = values.parents   # Discard last mapping

'''
merged = dict(b)
merged.update(a)    # not gonna to change the merged dict
'''
