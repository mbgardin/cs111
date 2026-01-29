import sys


def merge(left, right):
    """
    Merges two sorted lists into a single sorted list.

    Args:
        left (list): A sorted list.
        right (list): Another sorted list.

    Returns:
        list: A merged and sorted list.
    """
    merged = []
    i = j = 0
    # Continue until one of the lists is exhausted
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append the remaining elements from the non-exhausted list
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged


def merge_sort(data):
    """
    Recursively sorts a list using the merge sort algorithm.

    Args:
        data (list): The list to be sorted.

    Returns:
        list: A sorted version of the input list.
    """
    # Base case: a list of 0 or 1 elements is already sorted
    if len(data) <= 1:
        return data

    # Split the list in half
    mid = len(data) // 2
    left_half = merge_sort(data[:mid])
    right_half = merge_sort(data[mid:])

    # Merge the sorted halves
    return merge(left_half, right_half)


def read_file(filename):
    """
    Reads a file and returns a list of items.

    Args:
        filename (str): The name of the file to read.

    Returns:
        list: A list of items read from the file.
    """
    with open(filename, 'r') as file:
        return [line.strip() for line in file]


def write_file(filename, data):
    """
    Writes the data to the output file, one item per line, formatted with leading zeros.

    Args:
        filename (str): The name of the file to write to.
        data (list): The list of items to write.
    """
    with open(filename, 'w') as file:
        for item in data:
            # Format as a 3-digit number with leading zeros
            file.write(f"{int(item):03}\n")


if __name__ == "__main__":
    # Ensure the correct number of command-line arguments
    if len(sys.argv) != 3:
        print("Usage: python mergesort.py <inputfile> <outputfile>")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2]

    # Read the unsorted data from the input file
    unsorted_data = read_file(input_filename)

    # Try to convert the data to integers, fallback to keeping strings if it fails
    try:
        unsorted_data = [int(x) for x in unsorted_data]
    except ValueError:
        pass  # If data isn't numeric, keep it as strings

    # Sort the data using merge sort
    sorted_data = merge_sort(unsorted_data)

    # Write the sorted data to the output file
    write_file(output_filename, sorted_data)
