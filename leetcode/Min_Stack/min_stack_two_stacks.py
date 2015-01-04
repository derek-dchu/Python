
class MinStack:
    def __init__(self):
        self.data = []

        ## In order to have a constant time for retrieve the minimum element, we need to store it in another stack which has the same size
        self.min = []

    def push(self, x):
        """
        Push element x onto stack.
        :param x: pushed element
        :return: pushed element
        """
        if len(self.data) == 0 or x < self.min[len(self.min)-1]:
            self.min.append(x)
        else:
            self.min.append(self.min[len(self.min)-1])
        self.data.append(x)
        return x

    def pop(self):
        """
        Removes the element on top of the stack
        :return: top element
        """

        if len(self.data) == 0:
            return None
        self.min.pop()
        return self.data.pop()

    def top(self):
        if len(self.data) == 0:
            return None

        return self.data[len(self.data)-1]

    def getMin(self):
        return self.min[len(self.min)-1]

if __name__ == '__main__':
    test = MinStack()
    test.push(2147483646)
    test.push(2147483646)
    test.push(2147483647)
    assert(test.top() == 2147483647), "Not Match"
    assert(test.pop() == 2147483647), "Not Match"
    assert(test.getMin() == 2147483646), "Not Match"
    test.pop()
    test.getMin()
    test.pop()
    test.push(2147483647)
    test.top()
    test.getMin()
    test.push(-2147483648)
    test.top()
    assert(test.getMin() == -2147483648), "Not Match"
    test.pop()
    assert(test.getMin() == 2147483647), "Not Match"
