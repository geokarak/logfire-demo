from time import sleep


def fib(n: int) -> int:
    sleep(0.01)
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
