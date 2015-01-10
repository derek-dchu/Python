
class MinStack:
    def __init__(self):
        self.data = []

        ## In order to have a constant time for retrieve the minimum element, we need to store it. However,
        self.min = None

    def push(self, x):
        """
        Push element x onto stack.

        Args:
            x: pushed element

        Returns:
            pushed element
        """
        if len(self.data) == 0 or x < self.min:
            self.min = x

        self.data.append(x)
        return x

    def pop(self):
        """
        Removes the element on top of the stack

        Returns:
            top element
        """

        if len(self.data) == 0:
            return None
        x = self.data.pop()
        if len(self.data) != 0:
            self.updateMin()
        return x

    def top(self):
        if len(self.data) == 0:
            return None

        return self.data[len(self.data)-1]

    def getMin(self):
        return self.min

    def updateMin(self):
        self.min = self.data[0]
        for i in range(1, len(self.data)):
            if self.data[i] < self.min:
                self.min = self.data[i]

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

