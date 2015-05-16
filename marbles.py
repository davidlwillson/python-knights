#!/usr/bin/env python3
# What is the diff from that to just /usr/bin/python3?
# When do I put a docstring vs a shebang line?

# David L. Willson

# The point here is to practice some of the things in Chapter 2 of Dive Into Python 3.

print("I should review the logic stuph.")

a=True
b=True

c=True
d=False

e=False
f=True

g=False
h=False

print('a =', a, ' b =', b, 'a * b =', a*b)
print('c =', c, ' d =', d)

# A Tuple is an unchanging list

rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')

for col in rainbow_colors:
    print(col)
    
# A List is like an array
marbles=[0,]
x = 0
while x < 47:
    marbles[x]=rainbow_colors[x % 7]

print(marbles[22])

# A Set is like a bag of unique values
henry_bag=set(range(1,4))
print(henry_bag.pop())

# A Dictionary allows key/value storage.
'''
marbles[0]['color']='yellow'
marbles[0]['size']='70mm'
'''
