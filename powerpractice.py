'''square,cube,root,and power.

Available functions:

square(number)
    returns the square of a number

cube(number)
    returns the cube of a number

root(number)
    returns the square root of a number

power(number, power)
    returns then number to the power'th power

Example Usage:
>>> import powerpractice
>>> square(2)
4
>>> cube(2)
8
>>> root(9)
3
>>> power(9,0.5)
3
>>> power(3,2)
9

'''

def square(number=1):
    '''returns the square of a number'''
    return number * number

def cube(number=1):
    '''returns the cube of a number'''
    return number * number * number


if __name__ == '__main__':
    print( 'square of 2' )
    print( square(2) )
    print( 'cube of 2' )
    print( cube(2) )
