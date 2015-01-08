from math import ceil
from ..utils import swap, partition


def median_of_medians(iterable, left=None, right=None):
    """
    This method returns an approximate median using the median of medians algorithm

    :param: iterable    iterable data
    :param: left        left index
    :param: right       right index
    :return: a element of iterable data
    """
    if iterable is None:
        raise ValueError("The iterable is empty")
    if left is None:
        left = 0
    if right is None:
        right = len(iterable) - 1

    # divide the data into groups of five elements
    num_medians = int(ceil((right - left) / 5))
    for i in range(0, num_medians):
        sub_left = left + i*5
        sub_right = sub_left + 4
        if (sub_right > right):
            sub_right = right

        # get the median of each sub group using quick select
        median_index = quickselect_index(iterable, int((sub_right - sub_left) / 2), sub_left, sub_right)
        # move the median to a contiguous block at the beginning of the list
        swap(iterable, left+i, median_index)
        print(iterable)
    # select the median from the contiguous block
    median_of_medians_index = quickselect_index(iterable, left, left + num_medians - 1, int(num_medians / 2))
    return iterable[median_of_medians_index]

def quickselect_index(iterable, k, left=None, right=None):
        if iterable is None or k > len(iterable):
            raise ValueError("The iterable doesn't contain %d elements" % k)
        if left is None:
            left = 0
        if right is None:
            right = len(iterable)-1
        k += left
        while True:
            pivot = partition(iterable, left, right)
            if k == pivot:
                return k
            elif k < pivot:
                right = pivot - 1
            else:
                left = pivot + 1

if __name__ == '__main__':
    l = [1, 3, 2, 7, 5, 4, 6]
    print(median_of_medians(l)) # 4