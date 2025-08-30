def equilateral(sides):
    if checks(sides) is False:
        return False
    if sides[0] == sides[1] == sides[2]:
        return True
    return False

def isosceles(sides):
    if checks(sides) is False:
        return False
    conv_to_set = set(sides)
    if len(conv_to_set) <= 2:
        return True
    return False


def scalene(sides):
    if checks(sides) is False:
        return False
    conv_to_set = set(sides)
    if len(conv_to_set) == 3:
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