from ..utils import partition, random_list_gen


class k_th_min:
    """
    This method returns the kth smallest item in the array

    Args:
        iterable: an iterable object
        k: the kth smallest 

    Returns:
        The kth smallest item
    """
    # O(n log n), sort the array and return the kth item
    @staticmethod
    def sort_first(iterable, k):
        if iterable is None or k <= 0 or k > len(iterable):
            raise ValueError("Selected element out of bounds")

        iterable.sort()
        return iterable[k-1]

    # O(n) quickselect
    @staticmethod
    def quickselect(iterable, k):
        if iterable is None or k <= 0 or k > len(iterable):
            raise ValueError("Selected element out of bounds")

        k -= 1
        left = 0
        right = len(iterable)-1
        while right > left:
            pivot = partition(iterable, left, right)
            if pivot < k:
                left = pivot + 1
            elif pivot > k:
                right = pivot - 1
            else:
                return iterable[k]
        return iterable[left]

    @staticmethod
    def use_counter(iterable, k):
        if iterable is None or k <= 0 or k > len(iterable):
            raise ValueError("Selected element out of bounds")
        
        count = 0
        duplicate = 0
        next_min = float('Inf')
        l = len(iterable)

        for i in range(0, l):
            count = 0
            duplicate = 0
            if iterable[i] < next_min:
                for j in range(0, l):
                    if iterable[i] > iterable[j]:
                        count += 1
                        
                        if count >= k:
                            if iterable[i] < next_min:
                                next_min = iterable[i]
                            break
                    elif iterable[i] == iterable[j]:
                        duplicate += 1
                if count < k <= count + duplicate:
                    return iterable[i]


if __name__ == '__main__':
    for _ in range(0, 100):
        l = random_list_gen(99)
        l.append(1000)
        rst = k_th_min.sort_first(l, 10)
        assert(k_th_min.quickselect(l, 10) == rst)
        assert(k_th_min.use_counter(l, 10) == rst)

    from ..utils import Timer

    l = random_list_gen(100000)
    with Timer(True) as t:
        k_th_min.sort_first(l, 5)

    with Timer(True) as t:
        k_th_min.quickselect(l, 5)

    with Timer(True) as t:
        k_th_min.use_counter(l, 5)

