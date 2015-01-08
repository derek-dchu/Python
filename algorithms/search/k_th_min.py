from ..utils import partition

class k_th_min:
    """
    This method returns the kth smallest item in the array

    :param iterable: array of items
    :param k: 
    :return: item
    """
    # O(n log n), sort the array and return the kth item
    @staticmethod
    def sort_first(iterable, k):
        if iterable is None or k > len(iterable):
            raise ValueError("The iterable doesn't contain %d elements" % k)

        iterable.sort()
        return iterable[k-1]

    # O(n) quickselect
    @staticmethod
    def quickselect(iterable, k):
        k -= 1
        if iterable is None or k > len(iterable):
            raise ValueError("The iterable doesn't contain %d elements" % k)

        left = 0
        right = len(iterable)-1
        while True:
            pivot = partition(iterable, left, right)
            if k == pivot:
                return iterable[k]
            elif k < pivot:
                right = pivot - 1
            else:
                left = pivot + 1

if __name__ == '__main__':
    l = [1, 3, 2, 7, 5, 4]
    print(k_th_min.sort_first(l, 1)) # 1
    print(k_th_min.sort_first(l, 4)) # 4
    print(k_th_min.quickselect(l, 1)) # 1
    print(k_th_min.quickselect(l, len(l))) # 7
