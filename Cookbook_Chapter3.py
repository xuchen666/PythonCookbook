#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 10 15:31:08 2017

@author: xuchenwang
"""

# 3.1 Rounding numerical values
''' 
You want to round a floating-point number to a fixed number of decimal places.
'''

# round(value, ndigits)
round(1.2343,3)
round(12334,-2)
round(1.5,0)

x = 0.123456
format(x, '0.2f')
format(x, '0.3f')




# 3.2 Performing accurate decimal calculation
'''
You need to perform accurate calculations with decimal numbers, and don’t want 
the small errors that naturally occur with floats.
'''

from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
a+b

from decimal import localcontext
with localcontext() as ctx:
    ctx.prec = 3
    print(a/b)
    
'''
nums = [1.23e+18, 1, -1.23e+18]
sum(nums)   # Output: 0

import math
math.fsum(nums)
'''



# 3.3 Formatting numbers for output
'''
You need to format a number for output, controlling the number of digits, alignment, 
inclusion of a thousands separator, and other details.
'''
x = 1234.56789

format(x, '>10.1f')
'''
'[<>^]?width[,]?(.dig its)?' 
'[position: left/right/center][position of ,][position of .]'
'''

swap_operators = {ord('.'):',', ord(','):'.'}
format(x,',').translate(swap_operators)

'%0.2f' % x





# 3.4. Working with Binary, Octal, and Hexadecimal Integers
'''
You need to convert or output integers represented by binary, octal, or hexadecimal digits.
'''

x = 1234
bin(x)
oct(x)
hex(x)

format(x,'b')
format(x,'o')
format(x,'x')

int('4d2', 16)
int('10011010010', 2)

import os
os.chmod('script.py',0o755)






# 3.5. Packing and Unpacking Large Integers from Bytes
'''
You have a byte string and you need to unpack it into an integer value. Alternatively, 
you need to convert a large integer back into a byte string.
'''

data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
int.from_bytes(data,'little')   # the bytes order
int.from_bytes(data,'big')

x = 94522842520747284487117727783387188
x.to_bytes(16,'little')
x.to_bytes(16,'big')

# how many bits
nbytes, rem = divmod(x.bit_length(),8)
if rem:
    nbytes += 1
x.to_bytes(nbytes,'little')


import struct
hi,lo = struct.unpack('>QQ',data)
(hi<<64) + lo





# 3.6. Performing Complex-Valued Math
'''
Your code for interacting with the latest web authentication scheme has encountered a 
singularity and your only solution is to go around it in the complex plane. Or maybe you 
just need to perform some calculations using complex numbers.
'''

a = complex(2,4)
b = 3-5j
a.real, a.imag, a.conjugate()

import cmath
cmath.exp(a), cmath.cos(a), cmath.sin(a)





# 3.7. Working with Infinity and NaNs
'''
You need to create or test for the floating-point values of infinity, negative infinity, 
or NaN (not a number).
'''

a,b,c = float('inf'),float('-inf'),float('nan')
math.isinf(a), math.isnan(c)





# 3.8. Calculating with Fractions
'''
You have entered a time machine and suddenly find yourself working on elementary level 
homework problems involving fractions. Or perhaps you’re writing code to make calculations 
involving measurements made in your wood shop.
'''

from fractions import Fraction
a = Fraction(5,4)
a.numerator, a.denominator
float(a)
a.limit_denominator(8)

x = 3.75
y = Fraction(*x.as_integer_ratio())






# 3.9. Calculating with Large Numerical Arrays
'''
You need to perform calculations on large numerical datasets, such as arrays or grids.
'''

import numpy as np

ax = np.array([1,2,3,4])

grid = np.zeors(shape=(1000,1000),dtype=float)

a = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
a[1]            # select row 1
a[:,1]          # select column 1
a[1:3,1:3]      # select a sub region
a + [100,101,102,103]
np.where(a<10,a,10)






# 3.10. Performing Matrix and Linear Algebra Calculations
'''
You need to perform matrix and linear algebra operations, such as matrix multiplication, 
finding determinants, solving linear equations, and so on.
'''

m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
m.T   # transpose
m.I   # inverse

v = np.matrix([[2],[3],[4]])
m*v


import numpy.linalg
numpy.linalg.det(m)            # determinant
numpy.linalg.eigvals(m)        # eigenvalues
x = numpy.linalg.solve(m,v)    # mx = v






# 3.11. Picking Things at Random
'''
You want to pick random items out of a sequence or generate random numbers.
'''

import random

values = [1, 2, 3, 4, 5, 6]
random.choice(values)      # pick a random item out of a sequence
random.sample(values,3)    # take a sampling of N items
random.shuffle(values)     # shuffle items in a sequence in place
random.randint(0,10)       # produce random integers,
random.random()            # produce uniform floating-point values in the range 0 to 1
random.getrandbits(200)    # get N random-bits expressed as an integer

random.seed(3)
random.uniform(0,2)
random.gauss(0,1)





# 3.12. Converting Days to Seconds, and Other Basic Time Conversions
'''
You have code that needs to perform simple time conversions, like days to seconds, 
hours to minutes, and so on.
'''

from datetime import timedelta
a = timedelta(days=2, hours=6, minutes=2, seconds=30)
a.days,a.seconds

from datetime import datetime
a = datetime(2012,9,23,14,30,28)
b = datetime(2017,8,20)
b-a  # return timedelta
now = datetime.today()


from dateutil.relativedelta import relativedelta
a + relativedelta(months=+1)
d = relativedelta(b, a)
d.months,d.days





# 3.13. Determining Last Friday’s Date
'''
You want a general solution for finding a date for the last occurrence of a day of the week. 
Last Friday, for example.
'''

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
                'Friday', 'Saturday', 'Sunday']

def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7+day_num-day_num_target)%7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date-timedelta(days=days_ago)
    return target_date

get_previous_byday('Friday')


from dateutil.relativedelta import relativedelta
from dateutil.rrule import *
    
d = datetime.now()
d+relativedelta(weekday=FR)       # next Friday
d+relativedelta(weekday=FR(-1))   # last Friday








# 3.14. Finding the Date Range for the Current Month
'''
You have some code that needs to loop over each date in the current month, and 
want an efficient way to calculate that date range.
'''

from datetime import datetime, date, timedelta 
import calendar

def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year,start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date,end_date)

a_day = timedelta(days=1)
first_day,last_day = get_month_range()
while first_day<last_day:
    print(fist_day)
    first_day += a_day
    
    
def date_range(start,stop,step):
    while start<stop:
        yield start
        start += step
        
for d in date_range(datetime(2012, 9, 1), datetime(2012,10,1), timedelta(hours=6)):
    print(d)
    




# 3.15. Converting Strings into Datetimes
'''
Your application receives temporal data in string format, but you want to convert those 
strings into datetime objects in order to perform nonstring operations on them.
'''

text = '2012-09-20'
y = datetime.strptime(text,'%Y-%m-%d')
'''
%Y  4-digits year
%m  2-digits month
%d  day
%A  weekday
%B  month name
'''





# 3.16. Manipulating Dates Involving Time Zones
'''
You had a conference call scheduled for December 21, 2012, at 9:30 a.m. in Chicago. 
At what local time did your friend in Bangalore, India, have to show up to attend?
'''

from pytz import timezone

d = datetime(2012, 12, 21, 9, 30, 0)
central = timezone('US/Central')
loc_d = central.localize(d)
bang_d = loc_d.astimezone(timezone('Asia/Kolkata'))

d = datetime(2013, 3, 10, 1, 45)
loc_d = central.localize(d)
later = central.normalize(loc_d + timedelta(minutes=30))

    
utc_d = loc_d.astimezone(pytz.utc)
later_utc = utc_d + timedelta(minutes=30)
later_utc.astimezone(central)

# how to know the zone name
pytz.country_timezones['IN']









    

    