from functools import lru_cache


@lru_cache(maxsize=32)
def fib(n):
    if n < 2:
        return n
    return fib(n-1) + fib(n-2)


# fib.cache_clear()
print([fib(n) for n in range(20)])
