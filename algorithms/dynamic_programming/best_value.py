"""
Suppose we have a list of items with different weights
and values. However, we can carry only total w weights
of items. How to choose items to maximize the value.
"""


class Item:
    def __init__(self, id, weight, value):
        self.id = id
        self.weight = weight
        self.value = value


def solution(items, w):
    """
    :param items: a list of item objects
    :param w: a integer 
    """
    cache = {
        0: (0, -1, 0)
    }

    for i in range(1, w+1):
        cache[i] = None
        for item in (item for item in items if item.weight <= i):
            prev_weight = i - item.weight
            if prev_weight in cache and cache[prev_weight] is not None and isAvailable(cache, prev_weight, item.id):
                curr_value = cache[prev_weight][0] + item.value
                if cache[i] is None or curr_value > cache[i][0]:
                    cache[i] = (curr_value, prev_weight, item.id)

    return print_solution(cache, w)

def isAvailable(cache, w, id):
    while w in cache and cache[w] is not None:
        if cache[w][2] == id:
            return False
        w = cache[w][1]
    return True

def print_solution(cache, w):
    if w not in cache or cache[w] is None:
        return "weight not available"

    rst = "%d: " % cache[w][0]
    items = []
    while w != 0:
        items.append(cache[w][2])
        w = cache[w][1]
    return rst + str(items)


if __name__ == '__main__':
    items = [
        Item(1, 2, 3),
        Item(2, 3, 4),
        Item(3, 4, 8),
        Item(4, 5, 8),
        Item(5, 9, 10)
    ]

    print solution(items, 1) # weight not available
    print solution(items, 2) # 3: [1]
    print solution(items, 5) # 8: [4]
    print solution(items, 9) # 16: [3, 4]
    print solution(items, 18) # 26: [3, 4, 5]

