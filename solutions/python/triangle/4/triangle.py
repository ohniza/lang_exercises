def equilateral(sides):
    return sides[0] == sides[1] == sides[2] and checks(sides)


def isosceles(sides):
    return len(set(sides)) <= 2 and checks(sides)


def scalene(sides):
    return len(set(sides)) == 3 and checks(sides)


def checks(sides):
    for side in sides:
        if side <= 0:
            return False
    a, b, c = sides
    if a+b>c and b+c>a and a+c>b:
        return True
    else:
        return False