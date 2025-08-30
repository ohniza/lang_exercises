def leap_year(year):
    state = False
    if (year % 4 == 0):
        state = True
    if (year % 100 == 0):
        state = False
    if (year % 400 == 0):
        state = True
    
    return state
