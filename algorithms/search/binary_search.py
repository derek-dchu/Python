"""
Get a range of numbers from a sorted list using
binary search.
"""


def lower_bound(iterable, lo):
    """
    Search the smallest index of a sorted list that
    contains a number is equal to or larger than lo.
    This index will be the lower bound of range(lo, hi).

    :param iterable: a sorted list of numbers
    :param lo: an number as the lowest number within
               range [lo, hi]

    :return: lower bound as an index
    """
    data_len = len(data)
    # all numbers in the list are smaller than lo
    if data[data_len-1] < lo:
      return None

    l = 0
    r = data_len - 1
    while l < r:
        mid = int((r - l) / 2) + l
        if data[mid] == lo:
            lower_bound = mid
            break
        elif data[mid] > lo:
            r = mid - 1
        else:
            l = mid + 1

    if l == r:
        if data[l] >= lo:
            lower_bound = l
        else:
            lower_bound = l + 1
    return lower_bound

def upper_bound(iterable, hi):
    """
    Search the largest index of a sorted list that
    contains a number is equal to or smaller than hi.
    This index will be the upper bound of range(lo, hi).

    :param iterable: a sorted list of numbers
    :param hi: an number as the highest number within
               range [lo, hi]

    :return: upper bound as an index
    """
    data_len = len(data)
    # all numbers in the list are larger than lo
    if data[0] > hi:
      return None

    l = 0
    r = data_len - 1
    while l < r:
        mid = int((r - l) / 2) + l
        if data[mid] == hi:
            upper_bound = mid
            break
        elif data[mid] > hi:
            r = mid - 1
        else:
            l = mid + 1

    if l == r:
        if data[l] <= hi:
            upper_bound = l
        else:
            upper_bound = l - 1
    return upper_bound

def get_range(iterable, lo, hi):
    """
    Get all numbers within a sorted list that are
    within range [lo, hi].

    :param iterable: a sorted list of numbers
    :param lo: an number as the lowest number within
               range [lo, hi]
    :param hi: an number as the highest number within
               range [lo, hi]

    :return: a list of numbers
    """
    l = lower_bound(iterable, lo)
    u = upper_bound(iterable, hi)
    return iterable[l:u+1]


if __name__ == '__main__':

    data = [1,2,4,5,6,8,9]

    assert(lower_bound(data, 1) == 0)
    assert(lower_bound(data, 3) == 2)
    assert(lower_bound(data, 5) == 3)
    assert(lower_bound(data, 9) == 6)
    assert(lower_bound(data, 10) == None)

    assert(upper_bound(data, 1) == 0)
    assert(upper_bound(data, 3) == 1)
    assert(upper_bound(data, 7) == 4)
    assert(upper_bound(data, 9) == 6)
    assert(upper_bound(data, 0) == None)

    assert(get_range(data, 1, 9) == data)
    assert(get_range(data, 0, 10) == data)
    assert(get_range(data, 3, 7) == [4,5,6])
    assert(get_range(data, 0, 5) == [1,2,4,5])
    assert(get_range(data, 4, 10) == [4,5,6,8,9])

    assert(get_range(data, 8, 8) == [8])
    # Can't find number 7, return an empty list
    assert(get_range(data, 7, 7) == [])