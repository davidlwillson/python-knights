#!/usr/bin/env python3
# What is the diff from that to just /usr/bin/python3?
# When do I put a docstring vs a shebang line?

# David L. Willson

# The point here is to practice some of the logical things
# from Chapter 2 of Dive Into Python 3.

print("I should review the logic stuph.")
print("Multiplication acts like a logical 'and' and addition acts like a logical 'or'.")

a=True
b=True

print('a =', a, ' b =', b)
print('a * b =', a * b )
print('a + b =', a + b )

a=True
b=False

print('a =', a, ' b =', b)
print('a * b =', a * b )
print('a + b =', a + b )

a=False
b=True

print('a =', a, ' b =', b)
print('a * b =', a * b )
print('a + b =', a + b )

a=False
b=False

print('a =', a, ' b =', b)
print('a * b =', a * b )
print('a + b =', a + b )

print("Now, I wish I could remember how to typecast, so I can turn a 2 into a True.")
