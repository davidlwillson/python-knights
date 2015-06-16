'''
step fibonacci style
'''
def fib(max):
    a, b = 0,  1
    while a < max:
        yield a
        a, b = b, a + b

def fibsteps(steps):
    step = 0
    a, b = 0, 1
    while step < steps:
        yield a
        step = step + 1
        a, b = b, a + b
