import time

# 1
def powers(limit):
    return [x**2 for x in range(limit)]

# print(powers(5))

start = time.time()
powers = (500000000)
end = time.time()

print(end - start)


# 2
def measure_runtime(func):
    start = time.time()
    func()
    end = time.time()
    print(end - start) 
    
def powers(limit):
    return [x**2 for x in range(limit)]

measure_runtime(lambda: powers(50000000))


# 3
import timeit

print(timeit.timeit("[x**2 for x in range(10)]"))
print(timeit.timeit("list(map(lambda x: x**2, range(10)))"))
