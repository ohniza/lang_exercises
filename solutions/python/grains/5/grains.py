def square(number):
    # Returns the total number of grains on the square alone.
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return pow(2, number - 1)


def total():
    # Returns the total number of grains on the entire board
    total_grains = 0
    total_grains += square(number for number in range(1,64+1))
    return total_grains
