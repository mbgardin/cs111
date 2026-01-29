from pair import Pair, nil
from operator import add, sub, mul, truediv

# Task 1 - The reduce() Function
def reduce(func, operands, initial):
    result = initial
    while operands is not nil:
        result = func(result, operands.first)
        operands = operands.rest
    return result

# Task 2 - The apply() Function
def apply(operator, operands):
    if operator == "+":
        return reduce(add, operands, 0)
    elif operator == "-":
        return reduce(sub, operands.rest, operands.first)
    elif operator == "*":
        return reduce(mul, operands, 1)
    elif operator == "/":
        return reduce(truediv, operands.rest, operands.first)
    else:
        raise TypeError(f"Invalid operator: {operator}")

# Task 3 - Evaluating the Syntax Tree
def eval(syntax_tree):
    if isinstance(syntax_tree, int) or isinstance(syntax_tree, float):
        return syntax_tree
    elif isinstance(syntax_tree, Pair):
        operator = syntax_tree.first
        operands = syntax_tree.rest.map(eval)
        return apply(operator, operands)
    else:
        raise TypeError(f"Unknown expression: {syntax_tree}")

# Tokenize function from Lab 16
def tokenize(expression):
    """Converts a string expression into a list of tokens."""
    return expression.replace('(', ' ( ').replace(')', ' ) ').split()

# Parse tokens function (modified from Lab 16/Homework 6)
def parse_tokens(tokens, index):
    """Parses tokens recursively and builds a Pair expression tree."""
    if tokens[index] == '(':
        operator = tokens[index + 1]
        index += 2
        first = nil
        current_pair = nil
        while tokens[index] != ')':
            sub_expr, index = parse_tokens(tokens, index)
            if first is nil:
                first = Pair(sub_expr, nil)
                current_pair = first
            else:
                current_pair.rest = Pair(sub_expr, nil)
                current_pair = current_pair.rest
        return Pair(operator, first), index + 1
    elif tokens[index] == ')':
        return nil, index + 1
    else:
        try:
            if '.' in tokens[index]:
                operand = float(tokens[index])
            else:
                operand = int(tokens[index])
        except ValueError:
            raise TypeError(f"Invalid operand: {tokens[index]}")
        return operand, index + 1

# Parse function that hides the index detail
def parse(tokens):
    expression_tree, _ = parse_tokens(tokens, 0)
    return expression_tree

# Main loop for interactive calculator
def main():
    print("Welcome to the CS 111 Calculator Interpreter.")

    while True:
        # Print the prompt and get user input
        user_input = input("calc >> ")

        # Exit the loop if the user types 'exit'
        if user_input == "exit":
            print("Goodbye!")
            break

        try:
            # Tokenize the input
            tokens = tokenize(user_input)
            # Parse the tokens into an expression tree
            expression_tree = parse(tokens)
            # Evaluate the expression tree
            result = eval(expression_tree)
            # Print the result
            print(result)

        except Exception as e:
            # If there's an error, print it
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
