def square(number):
    # Returns the total number of grains on the square alone.
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return pow(2, number - 1)


def total():
    # Returns the total number of grains on the entire board
    total_grains = 0
    for number in range(1,64+1): #Since there are 64 squares on a box (range ends at 64 instead of 65)
        total_grains += square(number)
    return total_grains
