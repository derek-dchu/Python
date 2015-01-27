def shortest_sum(numbers, target):
    """
    Find the shortest sequence of available integers that sum up to a target integer

    :param number: a list of numbers
    :param target: a number

    :return: a list of numbers
    """
    if numbers is None or numbers == []:
        return []

    cache = {
        0: (-1, 0, 0)
    }
    for num_sum in range(target+1):
        seq_len = num_sum;
        available_numbers = (n for n in numbers if 0 < n <= num_sum)
        try:
            for num in available_numbers:
                if cache[num_sum-num][0] + 1 <= seq_len:
                    seq_len = cache[num_sum-num][0] + 1
                    cache[num_sum] = (seq_len, num)
        except (StopIteration, KeyError):
            cache[target] = None
    return sequence(target, cache)

def sequence(target, cache):
    """
    Construct a sequence of number from cache

    :param target: a number
    :param cache: a dictionary

    :return: a list of numbers
    """
    if target not in cache:
        return [];

    k = target
    seq = []
    while k > 0:
        if cache[k] is None:
            return []

        seq.append(cache[k][1])
        k = k - cache[k][1]
    return seq


if __name__ == '__main__':
    print(shortest_sum([1, 2], 3))  # [2,1]
    print(shortest_sum([], 3))      # []
    print(shortest_sum([3], 1))     # []
    print(shortest_sum([2], 3))     # []
    print(shortest_sum([1,5,10,25], 63)) # [25, 25, 10, 1, 1, 1]
    print(shortest_sum([1,5,8,10,25], 33))