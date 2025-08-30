def equilateral(sides):
    """
    Determine if a triangle is equilateral based on the length of its sides.

    Args:
        sides (list): A list of three integers representing the length of each side of the triangle.

    Returns:
        bool: True if the triangle is equilateral, False otherwise.
    """
    return sides[0] == sides[1] == sides[2] and checks(sides)


def isosceles(sides):
    """
    Determine if a triangle is isosceles based on the length of its sides.

    Args:
        sides (list): A list of three integers representing the length of each side of the triangle.

    Returns:
        bool: True if the triangle is isosceles, False otherwise.
    """
    return len(set(sides)) <= 2 and checks(sides)


def scalene(sides):
    """
    Determine if a triangle is scalene based on the length of its sides.

    Args:
        sides (list): A list of three integers representing the length of each side of the triangle.

    Returns:
        bool: True if the triangle is scalene, False otherwise.
    """
    return len(set(sides)) == 3 and checks(sides)


def checks(sides):
    """
    Check if the input sides form a valid triangle.

    Args:
        sides (list): A list of three integers representing the length of each side of the triangle.

    Returns:
        bool: True if the input sides form a valid triangle, False otherwise.
    """
    if 0 in sides:
        return False
    a, b, c = sides
    return a+b>c and b+c>a and a+c>b
