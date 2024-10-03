#!/usr/bin/python3
"""
0-main
"""
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
    print("\n")
    print_triangle(pascal_triangle(0))  # Edge case: should print nothing (empty list)
    print("\n")
    print_triangle(pascal_triangle(1))  # Edge case: should print just [[1]]
    print("\n")
    print_triangle(pascal_triangle(10))  # Test larger n
