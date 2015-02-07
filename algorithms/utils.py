import time
from random import randint

def swap(iterable, a, b):
    iterable[a], iterable[b] = iterable[b], iterable[a]

def partition(iterable, left, right):
    pivot = left + int((right - left) / 2)
    pivot_value = iterable[pivot]
    swap(iterable, pivot, right)
    storeIndex = left
    for i in range(left, right+1):
        if iterable[i] < pivot_value:
            swap(iterable, storeIndex, i)
            storeIndex += 1
    swap(iterable, storeIndex, right)
    return storeIndex

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Test
def random_list_gen(num):
    iterable = []
    for i in range(0, num):
        iterable.append(randint(0, num))
    return iterable

def is_sorted(iterable):
    for i in range(1, len(iterable)):
        if (iterable[i-1] > iterable[i]):
            return False
    return True


class Timer(object):
    def __init__(self, verbose=False):
        self.verbose = verbose

    def __enter__(self):
        self.start = time.time()
        return self

    def __exit__(self, *args):
        self.end = time.time()
        self.secs = self.end - self.start
        self.msecs = self.secs * 1000  # millisecs
        if self.verbose:
            print('elapsed time: %f ms' % self.msecs)

            