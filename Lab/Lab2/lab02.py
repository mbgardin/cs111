def even_weighted(s):
    """
    >>> x = [1, 2, 3, 4, 5, 6]
    >>> even_weighted(x)
    [0, 6, 20]
    """
    "*** YOUR CODE HERE ***"
    return [s[i] * i for i in range(len(s)) if i % 2 == 0]

# Example usage:
x = [1, 2, 3, 4, 5, 6]
print(even_weighted(x))  # Output: [0, 6, 20]

def couple(s, t):
    """Return a list of two-element lists in which the i-th element is [s[i], t[i]].

    >>> a = [1, 2, 3]
    >>> b = [4, 5, 6]
    >>> couple(a, b)
    [[1, 4], [2, 5], [3, 6]]
    >>> c = ['c', 6]
    >>> d = ['s', '1']
    >>> couple(c, d)
    [['c', 's'], [6, '1']]
    """
    assert len(s) == len(t)
    "*** YOUR CODE HERE ***"
    return [[s[i], t[i]] for i in range(len(s))]

a = [1, 2, 3]
b = [4, 5, 6]
print(couple(a, b))  # Output: [[1, 4], [2, 5], [3, 6]]

c = ['c', 6]
d = ['s', '1']
print(couple(c, d))  # Output: [['c', 's'], [6, '1']]




def count_appearances(lst):
    """Returns a dictionary containing each integer's appearance count
    >>> lst = [0]
    >>> count_appearances(lst)
    {0: 1}
    >>> lst = [0, 0, 1, 2, 1, 1]
    >>> count_appearances(lst)
    {0: 2, 1: 3, 2: 1}
    >>> lst = [0, 0, 0, 0, 0, 3, 0, 0]
    >>> count_appearances(lst)
    {0: 7, 3: 1}
    """
    "*** YOUR CODE HERE ***"
    count_dict = {}
    for num in lst:
        if num in count_dict:
            count_dict[num] += 1
        else:
                count_dict[num] = 1
    return count_dict

lst = [0]
print(count_appearances(lst))  # Output: {0: 1}

lst = [0, 0, 1, 2, 1, 1]
print(count_appearances(lst))  # Output: {0: 2, 1: 3, 2: 1}

lst = [0, 8, 0, 8, 0, 3, 3, 0, 8]
print(count_appearances(lst))  # Output: {0: 4, 8: 3, 3: 2}


def copy_file(input_filename, output_filename):
    """Print each line from input with the line number and a colon prepended,
    then write that line to the output file.
    >>> copy_file('text.txt', 'output.txt')
    1: They say you should never eat dirt.
    2: It's not nearly as good as an onion.
    3: It's not as good as the CS pun on my shirt.
    """
    "*** YOUR CODE HERE ***"
    with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
        for line_number, line in enumerate(infile, start=1):
            formatted_line = f"{line_number}: {line}"
            print(formatted_line, end = ' ')  # Print to console
            outfile.write(formatted_line)  # Write to output file
            copy_file('text.txt', 'output.txt')


########################################################
# OPTIONAL QUESTIONS


def factors_list(n):
    """Return a list containing all the numbers that divide `n` evenly, except
    for the number itself. Make sure the list is in ascending order.

    >>> factors_list(6)
    [1, 2, 3]
    >>> factors_list(8)
    [1, 2, 4]
    >>> factors_list(28)
    [1, 2, 4, 7, 14]
    """
    all_factors = []
    # Write your code here


def slice_and_multiplice(lst):
    """Return a new list where all values past the first are
    multiplied by the first value.

    >>> slice_and_multiplice([1,1,6])
    [1, 6]
    >>> slice_and_multiplice([9,1,5,2])
    [9, 45, 18]
    >>> slice_and_multiplice([4])
    []
    >>> slice_and_multiplice([0,4,9,18,20])
    [0, 0, 0, 0]
    """
    # Write your code here
