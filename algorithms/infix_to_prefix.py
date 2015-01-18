"""
This script convert infix expression to prefix

algorithm:
    Scan the token list from right to left
        * if the token is an operand, append to output
        * if the token is a right parenthesis, push it on the stack
        * if the token is a left parenthesis, pop the stack until meet a right parenthesis. Append each operator to the left of output
        * if the token is an operator, first remove any operators already on the stack that have higher or equal precedence and append them to the left of output.
    Append the rest of operators in stack to the left of output
"""
from collections import deque
from data_structure.stack import Stack


def infix_to_preifx(expr):
    """
    convert infix to prefix

    Args:
        expr: an infix expression in the form of '1 * ( 2 + 3 )'.

    Returns:
        An prefix expression.
    """
    # precedence dict
    prec = {
        "^": 4,
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        ")": 1
    }

    stack = Stack()
    tokens = expr.split()

    prefix_expr = deque()
    # scan from right to left
    for token in reversed(tokens):
        # Find a right parenthesis
        if token == ')':
            stack.push(token)
        # Find a left parenthesis
        elif token == '(':
            top_token = stack.pop()
            while top_token != ')':
                prefix_expr.appendleft(top_token)
                top_token = stack.pop()
        # Find an operator
        elif token in prec:
            while not stack.isEmpty() and prec[stack.peek()] >= prec[token]:
                prefix_expr.appendleft(stack.pop())
            stack.push(token)
        # Find an operand
        else:
            prefix_expr.appendleft(token)

    while not stack.isEmpty():
        prefix_expr.appendleft(stack.pop())
    return " ".join(prefix_expr)


if __name__ == '__main__':
    test1 = "( A + B ) * C - ( D - E ) * ( F + G )"
    answer1 = "- * + A B C * - D E + F G"
    assert(infix_to_preifx(test1) == answer1), "Answer is not correct"

    test2 = "5 * 3 ^ ( 4 - 2 )"
    answer2 = "* 5 ^ 3 - 4 2"
    assert(infix_to_preifx(test2) == answer2), "Answer is not correct"