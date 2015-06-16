'''
step fibonacci style
'''
def fib(max=0):
    a, b = 0,  1
    if max>0:
        while a < max:
            yield a
            a, b = b, a + b
    else:
        yield a
        a, b = b, a + b
