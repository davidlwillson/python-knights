Python 3.4.0 (default, Apr 11 2014, 13:05:11) 
[GCC 4.8.2] on linux
Type "copyright", "credits" or "license()" for more information.
>>> ================================ RESTART ================================
>>> 
rainbow_colors ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh ('two', 'three', '...', 'king', 'ace')
If I were smart, I would be able to build card_ranks_acelow from card_ranks_acehigh
red
orange
yellow
green
blue
purple
Traceback (most recent call last):
  File "/home/dlwillson/git/python-knights/marbles.py", line 32, in <module>
    print ('marbles[',x,']=', marbles[x])
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
If I were smart, I would be able to build card_ranks_acelow from card_ranks_acehigh
red
orange
yellow
green
blue
purple
x = 0
marbles[ 0 ]= red
x = 1
Traceback (most recent call last):
  File "/home/dlwillson/git/python-knights/marbles.py", line 31, in <module>
    marbles[x]=rainbow_colors[x % 7]
IndexError: list assignment index out of range
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
If I were smart, I would be able to build card_ranks_acelow from card_ranks_acehigh
red
orange
yellow
green
blue
purple
x = 0
x % 7 = 0
marbles[ 0 ]= 0
x = 1
x % 7 = 1
marbles[ 1 ]= red
x = 2
x % 7 = 2
marbles[ 2 ]= orange
x = 3
x % 7 = 3
marbles[ 3 ]= yellow
x = 4
x % 7 = 4
marbles[ 4 ]= green
x = 5
x % 7 = 5
marbles[ 5 ]= blue
x = 6
x % 7 = 6
Traceback (most recent call last):
  File "/home/dlwillson/git/python-knights/marbles.py", line 32, in <module>
    marbles.append(rainbow_colors[x % 7])
IndexError: tuple index out of range
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
If I were smart, I would be able to build card_ranks_acelow from card_ranks_acehigh
red
orange
yellow
green
blue
purple
x = 0
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 0 ]= 0
x = 1
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 1 ]= red
x = 2
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 2 ]= orange
x = 3
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 3 ]= yellow
x = 4
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 4 ]= green
x = 5
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 5 ]= blue
x = 6
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 6 ]= purple
x = 7
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 7 ]= red
x = 8
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 8 ]= orange
x = 9
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 9 ]= yellow
x = 10
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 10 ]= green
x = 11
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 11 ]= blue
x = 12
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 12 ]= purple
x = 13
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 13 ]= red
x = 14
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 14 ]= orange
x = 15
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 15 ]= yellow
x = 16
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 16 ]= green
x = 17
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 17 ]= blue
x = 18
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 18 ]= purple
x = 19
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 19 ]= red
x = 20
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 20 ]= orange
x = 21
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 21 ]= yellow
x = 22
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 22 ]= green
x = 23
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 23 ]= blue
x = 24
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 24 ]= purple
x = 25
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 25 ]= red
x = 26
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 26 ]= orange
x = 27
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 27 ]= yellow
x = 28
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 28 ]= green
x = 29
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 29 ]= blue
x = 30
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 30 ]= purple
x = 31
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 31 ]= red
x = 32
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 32 ]= orange
x = 33
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 33 ]= yellow
x = 34
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 34 ]= green
x = 35
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 35 ]= blue
x = 36
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 36 ]= purple
x = 37
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 37 ]= red
x = 38
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 38 ]= orange
x = 39
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 39 ]= yellow
x = 40
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 40 ]= green
x = 41
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 41 ]= blue
x = 42
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 42 ]= purple
x = 43
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 43 ]= red
x = 44
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 44 ]= orange
x = 45
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 45 ]= yellow
x = 46
<built-in method index of tuple object at 0x7fb24b620c48>
marbles[ 46 ]= green
henry_bag = {1, 2, 3}
1
2
3
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
If I were smart, I would be able to build card_ranks_acelow from card_ranks_acehigh
red
orange
yellow
green
blue
purple
marbles = [0, 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue']
henry_bag = {1, 2, 3}
1
2
3
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
If I were smart, I would be able to build card_ranks_acelow from card_ranks_acehigh
red
orange
yellow
green
blue
purple
marbles = [0, 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue']
range(1, 4)
henry_bag = {1, 2, 3}
1
2
3
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
If I were smart, I would be able to build card_ranks_acelow from card_ranks_acehigh
red
orange
yellow
green
blue
purple
marbles = [0, 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue']
henry_bag = {0, 'purple', 'orange', 'yellow', 'red', 'blue', 'green'}
0
purple
orange
yellow
red
blue
green
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
If I were smart, I would be able to build card_ranks_acelow from card_ranks_acehigh
red
orange
yellow
green
blue
purple
marbles = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue']
henry_bag = {'green', 'purple', 'blue', 'red', 'orange', 'yellow'}
green
purple
blue
red
orange
yellow
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
If I were smart, I would be able to build card_ranks_acelow from card_ranks_acehigh
red
orange
yellow
green
blue
purple
marbles = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue']
Watch while Henry's amazing bag removes all the duplicate marbles!
henry_bag = {'red', 'green', 'blue', 'purple', 'yellow', 'orange'}
Cool, huh?
Traceback (most recent call last):
  File "/home/dlwillson/git/python-knights/marbles.py", line 45, in <module>
    marble[0]=dict()
NameError: name 'marble' is not defined
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
If I were smart, I would be able to build card_ranks_acelow from card_ranks_acehigh
red
orange
yellow
green
blue
purple
marbles = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue']
Watch while Henry's amazing bag removes all the duplicate marbles!
henry_bag = {'yellow', 'blue', 'purple', 'orange', 'green', 'red'}
Cool, huh?
[{'size': '70mm', 'color': 'yellow'}, 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue']
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
card_ranks_acelow = ('ace', ('two', 'three', '...'))
If I were smart, I would be able to build card_ranks_acelow from card_ranks_acehigh
red
orange
yellow
green
blue
purple
marbles = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue']
Watch while Henry's amazing bag removes all the duplicate marbles!
henry_bag = {'blue', 'green', 'red', 'orange', 'yellow', 'purple'}
Cool, huh?
[{'color': 'yellow', 'size': '70mm'}, 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue']
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
card_ranks_acelow = ('ace', ['two', 'three', '...'])
If I were smart, I would be able to build card_ranks_acelow from card_ranks_acehigh
red
orange
yellow
green
blue
purple
marbles = ['red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue']
Watch while Henry's amazing bag removes all the duplicate marbles!
henry_bag = {'orange', 'blue', 'red', 'yellow', 'green', 'purple'}
Cool, huh?
[{'size': '70mm', 'color': 'yellow'}, 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue']
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
card_ranks_acelow = ('ace', ['two', 'three', '...'])
If I were smarter, I would be able to build card_ranks_acelow from card_ranks_acehigh
red
orange
yellow
green
blue
purple
Traceback (most recent call last):
  File "/home/dlwillson/git/python-knights/marbles.py", line 42, in <module>
    marbles_abbr = marbles[0:2] + '...' + marbles[-3:-1]
TypeError: can only concatenate list (not "str") to list
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
card_ranks_acelow = ('ace', ['two', 'three', '...'])
If I were smarter, I would be able to build card_ranks_acelow from card_ranks_acehigh
red
orange
yellow
green
blue
purple
['red', 'orange', '...', 'yellow', 'green']
Watch while Henry's amazing bag removes all the duplicate marbles!
henry_bag = {'red', 'yellow', 'blue', 'purple', 'orange', 'green'}
Cool, huh?
[{'size': '70mm', 'color': 'yellow'}, 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue', 'purple', 'red', 'orange', 'yellow', 'green', 'blue']
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
card_ranks_acelow = ('ace', ['two', 'three', '...'])
If I were smarter, I would be able to build card_ranks_acelow from card_ranks_acehigh
red
orange
yellow
green
blue
purple
marbles = ['red', 'orange', 'yellow', 'green', 'blue']
Watch while Henry's amazing bag removes all the duplicate marbles!
henry_bag = {'red', 'orange', 'yellow', 'blue', 'green'}
Cool, huh?
[[{'color': 'yellow', 'size': '70mm'}, 'orange', 'yellow', '...']]
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
card_ranks_acelow = ('ace', ['two', 'three', '...'])
If I were smarter, I would be able to build card_ranks_acelow from card_ranks_acehigh
red
orange
yellow
green
blue
purple
marbles = ['red', 'orange', 'yellow', 'green', 'blue']
Watch while Henry's amazing bag removes all the duplicate marbles!
henry_bag = {'yellow', 'orange', 'green', 'blue', 'red'}
Cool, huh?
[{'size': '70mm', 'color': 'yellow'}, 'orange', 'yellow', '...']
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
card_ranks_acelow = ['a', 'c', 'e', 'two', 'three', '...']
If I were smarter, I would be able to build card_ranks_acelow from card_ranks_acehigh
red
orange
yellow
green
blue
purple
['red', 'orange', '...', 'purple', 'red']
Watch while Henry's amazing bag removes all the duplicate marbles!
henry_bag = {'yellow', 'orange', 'red', 'purple', 'blue', 'green'}
Cool, huh?
[{'size': '70mm', 'color': 'yellow'}, 'orange', 'yellow', '...']
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
Traceback (most recent call last):
  File "/home/dlwillson/git/python-knights/marbles.py", line 22, in <module>
    card_ranks_acelow = (card_ranks_acehigh[-1]+list(card_ranks_acehigh[0:-1]))
TypeError: Can't convert 'list' object to str implicitly
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
Traceback (most recent call last):
  File "/home/dlwillson/git/python-knights/marbles.py", line 22, in <module>
    card_ranks_acelow = (str(card_ranks_acehigh[-1])+list(card_ranks_acehigh[0:-1]))
TypeError: Can't convert 'list' object to str implicitly
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
Traceback (most recent call last):
  File "/home/dlwillson/git/python-knights/marbles.py", line 22, in <module>
    card_ranks_acelow = (card_ranks_acehigh[-1]+card_ranks_acehigh[0:-1])
TypeError: Can't convert 'tuple' object to str implicitly
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
red
orange
yellow
green
blue
purple
['red', 'orange', 'yellow', '...']
Watch while Henry's amazing bag removes all the duplicate marbles!
henry_bag = {'orange', 'blue', 'yellow', 'green', 'red', 'purple'}
Cool, huh?
[{'size': '70mm', 'color': 'yellow'}, 'orange', 'yellow', '...']
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
red
orange
yellow
green
blue
purple
['red', 'orange', 'yellow', '...']
Watch while Henry's amazing bag removes all the duplicate marbles!
henry_bag = {'yellow', 'red', 'green', 'purple', 'orange', 'blue'}
Cool, huh?
[{'size': '70mm', 'color': 'yellow'}, 'orange', 'yellow', '...']
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
red
orange
yellow
green
blue
purple
['red', 'orange', 'yellow', '...']
Watch while Henry's amazing bag removes all the duplicate marbles!
henry_bag = {'blue', 'orange', 'red', 'purple', 'yellow', 'green'}
Cool, huh?
[{'color': 'yellow', 'size': '70mm'}, 'orange', 'yellow', '...']
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
red
orange
yellow
green
blue
purple
['red', 'orange', 'yellow', '...', 'purple', 'red']
Traceback (most recent call last):
  File "/home/dlwillson/git/python-knights/marbles.py", line 44, in <module>
    print ('last_marble =', marbles[len(marbles)+1])
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
red
orange
yellow
green
blue
purple
['red', 'orange', 'yellow', '...', 'purple', 'red']
Traceback (most recent call last):
  File "/home/dlwillson/git/python-knights/marbles.py", line 44, in <module>
    print ('last_marble =', marbles[len(marbles)])
IndexError: list index out of range
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
red
orange
yellow
green
blue
purple
['red', 'orange', 'yellow', '...', 'purple', 'red']
last_marble = orange
Watch while Henry's amazing bag removes all the duplicate marbles!
henry_bag = {'green', 'purple', 'red', 'yellow', 'orange', 'blue'}
Cool, huh?
[{'size': '70mm', 'color': 'yellow'}, 'orange', 'yellow', '...']
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
red
orange
yellow
green
blue
purple
['red', 'orange', 'yellow', '...']
first_marble =  red
last_marble = orange
Watch while Henry's amazing bag removes all the duplicate marbles!
henry_bag = {'blue', 'yellow', 'green', 'red', 'purple', 'orange'}
Cool, huh?
[{'size': '70mm', 'color': 'yellow'}, 'orange', 'yellow', '...']
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
red
orange
yellow
green
blue
purple
[]
['red', 'orange', 'yellow', '...']
first_marble =  red
last_marble = orange
Watch while Henry's amazing bag removes all the duplicate marbles!
henry_bag = {'green', 'orange', 'red', 'blue', 'purple', 'yellow'}
Cool, huh?
[{'size': '70mm', 'color': 'yellow'}, 'orange', 'yellow', '...']
>>> 
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
red
orange
yellow
green
blue
purple
last three marbles []
['red', 'orange', 'yellow', '...']
first marble = red
last marble = orange
Watch while Henry's amazing bag removes all the duplicate marbles!
henry_bag = {'green', 'red', 'purple', 'orange', 'blue', 'yellow'}
Cool, huh?
[{'color': 'yellow', 'size': '70mm'}, 'orange', 'yellow', '...']
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
red
orange
yellow
green
blue
purple
last three marbles ['red', 'orange', 'yellow']
['red', 'orange', 'yellow', '...', 'red', 'orange', 'yellow']
first marble = red
last marble = orange
Watch while Henry's amazing bag removes all the duplicate marbles!
henry_bag = {'purple', 'red', 'blue', 'green', 'yellow', 'orange'}
Cool, huh?
[{'color': 'yellow', 'size': '70mm'}, 'orange', 'yellow', '...']
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
red
orange
yellow
green
blue
purple
last three marbles ['red', 'orange', 'yellow']
['red', 'orange', 'yellow', '...', 'red', 'orange', 'yellow']
first marble = red
last marble = orange
Watch while Henry's amazing bag removes all the duplicate marbles!
henry_bag = {'red', 'yellow', 'blue', 'green', 'orange', 'purple'}
Cool, huh?
[{'color': 'yellow', 'size': '70mm'}, 'orange', 'yellow', '...']
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
red
orange
yellow
green
blue
purple
last three marbles ['purple', 'red', 'orange']
['red', 'orange', 'yellow', '...', 'purple', 'red', 'orange']
first marble = red
last marble = orange
Watch while Henry's amazing bag removes all the duplicate marbles!
henry_bag = {'blue', 'purple', 'red', 'yellow', 'green', 'orange'}
Cool, huh?
[{'size': '70mm', 'color': 'yellow'}, 'orange', 'yellow', '...']
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
red
orange
yellow
green
blue
purple
last three marbles ['purple', 'red', 'orange']
['red', 'orange', 'yellow', '...', 'purple', 'red', 'orange']
first marble = red
last marble = orange
Watch while Henry's amazing bag removes all the duplicate marbles!
henry_bag = {'orange', 'green', 'purple', 'blue', 'red', 'yellow'}
Cool, huh?
[{'size': '70mm', 'color': 'yellow'}, 'orange', 'yellow', '...']
>>> ================================ RESTART ================================
>>> 
rainbow_colors = ('red', 'orange', 'yellow', 'green', 'blue', 'purple')
card_suits = ('spades', 'clubs', 'hearts', 'diamonds')
card_ranks_acehigh = ('two', 'three', '...', 'king', 'ace')
red
orange
yellow
green
blue
purple
last three marbles ['purple', 'red', 'orange']
['red', 'orange', 'yellow', '...', 'purple', 'red', 'orange']
first marble = red
last marble = orange
Watch while Henry's amazing bag removes all the duplicate marbles!
henry_bag = {'blue', 'orange', 'purple', 'green', 'yellow', 'red'}
Cool, huh?
[{'color': 'yellow', 'size': '70mm'}, 'orange', 'yellow', '...']
>>> 
