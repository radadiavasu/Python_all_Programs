from functools import wraps
from time import perf_counter

def memorize(func):
    catch = {}
    
    @wraps(func)
    def wrapper(*args , **kwargs):
        key = str(args) + str(kwargs)
        
        if key not in catch:
            catch[key] = func(*args , **kwargs)
        return catch[key]
    return wrapper

@memorize
def fibonacci(n: int):
    if n < 2:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

if __name__ == '__main__':
    start = perf_counter()
    f = fibonacci(60)
    end = perf_counter()
    print(f)
    print(f"Total Estimate Time: {end - start}")