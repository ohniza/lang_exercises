def equilateral(sides):
    if sides[0] == sides[1] == sides[2] and checks(sides):
        return True
    return False

def isosceles(sides):
    conv_to_set = set(sides)
    if len(conv_to_set) <= 2 and checks(sides):
        return True
    return False


def scalene(sides):
    conv_to_set = set(sides)
    if len(conv_to_set) == 3 and checks(sides):
        return True
    return False

def checks(sides):
    for side in sides:
        if side <= 0:
            return False
    (a, b, c) = (sides[0], sides[1], sides[2])
    check1 = a + b >= c
    check2 = b + c >= a
    check3 = a + c >= b
    return check1 and check2 and check3