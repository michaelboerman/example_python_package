# https://packaging.python.org/en/latest/tutorials/packaging-projects/

def add_one(number):
    if not isinstance(number, (int, float)):
        raise TypeError("Input value must be an integer or float")
    return number + 1

def subtract_one(number):
    if not isinstance(number, (int, float)):
        raise TypeError("Input value must be an integer or float")
    return number - 1