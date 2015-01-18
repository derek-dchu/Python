"""
This script convert infix expression to postfix

algorithm:
    Scan the token list from left to right
        * if the token is an operand, append to output
        * if the token is a left parenthesis, push it on the stack
        * if the token is a right parenthesis, pop the stack until meet a left parenthesis. Append each operator to output
        * if the token is an operator, first remove any operators already on the stack that have higher or equal precedence and append them to output.
    Append the rest of operators in stack to output
"""
from data_structure.stack import Stack


def infix_to_postifx(expr):
    """
    convert infix to postfix

    Args:
        expr: an infix expression in the form of '1 * ( 2 + 3 )'.

    Returns:
        An postfix expression of the same form.
    """
    # precedence dict
    prec = {
        "^": 4,
        "*": 3,
        "/": 3,
        "+": 2,
        "-": 2,
        "(": 1
    }

    stack = Stack()
    tokens = expr.split()

    postfix_expr = []
    for token in tokens:
        # Find a left parenthesis
        if token == '(':
            stack.push(token)
        # Find a right parenthesis
        elif token == ')':
            top_token = stack.pop()
            while top_token != '(':
                postfix_expr.append(top_token)
                top_token = stack.pop()
        # Find an operator
        elif token in prec:
            while not stack.isEmpty() and prec[stack.peek()] >= prec[token]:
                postfix_expr.append(stack.pop())
            stack.push(token)
        # Find an operand
        else:
            postfix_expr.append(token)

    while not stack.isEmpty():
        postfix_expr.append(stack.pop())
    return " ".join(postfix_expr)


if __name__ == '__main__':
    test1 = "( A + B ) * C - ( D - E ) * ( F + G )"
    answer1 = "A B + C * D E - F G + * -"
    assert(infix_to_postifx(test1) == answer1), "Answer is not correct"

    test2 = "5 * 3 ^ ( 4 - 2 )"
    answer2 = "5 3 4 2 - ^ *"
    assert(infix_to_postifx(test2) == answer2), "Answer is not correct"
