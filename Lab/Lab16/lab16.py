# lab16.py

from pair import *


def tokenize(expression):
    """ Takes a string and returns a list where each item
    in the list is a parenthesis, one of the four operators (/, *, -, +),
    or a number literal.

    Args:
        expression (str): A string expression in prefix notation.

    Returns:
        list: A list of tokens, each representing either a parenthesis, operator, or number literal.

    Examples:
        >>> tokenize("(+ 3 2)")
        ['(', '+', '3', '2', ')']
        >>> tokenize("(- 9 3 3)")
        ['(', '-', '9', '3', '3', ')']
        >>> tokenize("(+ 10 100)")
        ['(', '+', '10', '100', ')']
        >>> tokenize("(+ 5.5 10.5)")
        ['(', '+', '5.5', '10.5', ')']
        >>> expr = "(* (- 8 4) 4)"
        >>> tokenize(expr)
        ['(', '*', '(', '-', '8', '4', ')', '4', ')']
        >>> expr = "(* (- 6 8) (/ 18 3) (+ 10 1 2))"
        >>> tokenize(expr)
        ['(', '*', '(', '-', '6', '8', ')', '(', '/', '18', '3', ')', '(', '+', '10', '1', '2', ')', ')']
    """
    # Add spaces around parentheses and split by spaces
    expression = expression.replace('(', ' ( ').replace(')', ' ) ')
    return expression.split()


def parse_tokens(tokens, index):
    """ Takes a list of tokens and an index and converts the tokens to a Pair list

    Args:
        tokens (list): A list of tokens from the tokenize function.
        index (int): The current index in the list of tokens.

    Returns:
        tuple: A Pair object and the updated index.

    Examples:
        >>> parse_tokens(['(', '+', '1', '1', ')'], 0)
        (Pair('+', Pair(1, Pair(1, nil))), 5)
        >>> parse_tokens(['(', '*', '(', '-', '8', '4', ')', '4', ')'], 0)
        (Pair('*', Pair(Pair('-', Pair(8, Pair(4, nil))), Pair(4, nil))), 9)
    """
    if tokens[index] == '(':
        # Get the operator (next token after '(')
        operator = tokens[index + 1]
        # Parse the rest of the tokens
        rest, index = parse_tokens(tokens, index + 2)
        # Return Pair of the operator and operands
        return Pair(operator, rest), index

    elif tokens[index] == ')':
        # Closing parenthesis indicates end of a sub-expression
        return nil, index + 1

    else:
        # Operand (either an int or a float)
        try:
            if '.' in tokens[index]:
                operand = float(tokens[index])
            else:
                operand = int(tokens[index])
        except ValueError:
            raise TypeError(f"Invalid operand: {tokens[index]}")

        # Recursively parse the rest of the tokens
        rest, index = parse_tokens(tokens, index + 1)
        return Pair(operand, rest), index


if __name__ == "__main__":
    import doctest

    doctest.testmod()
