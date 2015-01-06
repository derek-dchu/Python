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