# calculator.py

from pair import Pair, nil


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
    expression = expression.replace('(', ' ( ').replace(')', ' ) ')
    return expression.split()


from pair import Pair, nil


def parse_tokens(tokens, index):
    """
    Recursively converts a list of tokens into a Pair list structure.

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

    # Check if the current token is an opening parenthesis
    if tokens[index] == '(':
        # The next token should be the operator (e.g., '+', '-', '*', '/')
        operator = tokens[index + 1]
        index += 2  # Move past '(' and operator

        # Initialize an empty pair list for the operands
        first = nil  # This holds the first operand, starting with nil
        current_pair = nil  # Tracks the current pair as we build the list

        # Parse the operands
        while tokens[index] != ')':  # Until the closing parenthesis is found
            sub_expr, index = parse_tokens(tokens, index)  # Parse the next operand

            if first is nil:  # If it's the first operand, initialize the list
                first = Pair(sub_expr, nil)
                current_pair = first
            else:  # For subsequent operands, link them
                current_pair.rest = Pair(sub_expr, nil)
                current_pair = current_pair.rest

        # Return the completed Pair structure
        return Pair(operator, first), index + 1  # Skip past the closing parenthesis

    # If the token is not a parenthesis, it's an operand (int or float)
    else:
        try:
            if '.' in tokens[index]:
                operand = float(tokens[index])  # It's a float
            else:
                operand = int(tokens[index])  # It's an int
        except ValueError:
            raise TypeError(f"Invalid operand: {tokens[index]}")

        # Return the operand as a Pair and move to the next token
        return operand, index + 1


if __name__ == "__main__":
    import doctest

    doctest.testmod()
