from data_structure.stack import Stack


class Solution:
    """
    Returns:
        a boolean
    """
    def isValid(self, s):
        # unbalance number of parentheses
        if len(s) % 2 != 0:
            return False

        left_parentheses = ['(', '{', '[']
        right_parentheses = [')', '}', ']']
        stack = Stack()

        for c in s:
            if c in left_parentheses:
                stack.push(c)
            elif stack.isEmpty() or stack.peek() != left_parentheses[right_parentheses.index(c)]:
                return False
            else:
                stack.pop()

        return stack.isEmpty()