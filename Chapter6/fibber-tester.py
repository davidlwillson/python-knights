from fibber import fib, fibsteps

for n in fib(1000):
    print(n, end=' ')

print("\n---\n")

for m in fibsteps(100):
    print('m =',m , end=',')
