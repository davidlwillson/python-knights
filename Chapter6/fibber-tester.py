from fibber import fib

for n in fib(1000):
    print(n, end=' ')


for step in range(1,100):
    print('step = %s', step)
    print(fib())
