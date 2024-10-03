def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal’s triangle of n.
    """
    if n <= 0:
        return []

    # Initialize Pascal's triangle with the first row
    triangle = [[1]]

    for i in range(1, n):
        prev_row = triangle[-1]  # Get the previous row
        new_row = [1]  # Every row starts with 1

        # Compute the values inside the row (excluding the first and last 1)
        for j in range(1, i):
            new_row.append(prev_row[j - 1] + prev_row[j])

        new_row.append(1)  # Every row ends with 1
        triangle.append(new_row)

    return triangle
