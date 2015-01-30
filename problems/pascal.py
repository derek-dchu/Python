def pascal(n):
    """
    Prints out Pascal's triangle.

    :param n: number of rows
    """
    if n < 1:
        return
    print " " * (n - 1) + "1"
    if n < 2:
        return
    print " " * (n - 2) + "1 1"
    if n < 3:
        return

    prev_row = [1, 1]
    for i in range(3, n+1):
        curr_row = [1]
        row = "1 "
        for j in range(1, i-1):
            num = prev_row[j-1] + prev_row[j]
            row += "%d " % num
            curr_row.append(num)
        curr_row.append(1)
        print " " * (n - i) + row + "1"
        prev_row = curr_row


if __name__ == '__main__':
    pascal(5)

    '''
        1
       1 1
      1 2 1
     1 3 3 1
    1 4 6 4 1
    '''
