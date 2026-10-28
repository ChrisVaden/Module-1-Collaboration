

def square_number(value):
    if not isinstance(value, (int, float)):
        raise TypeError("Input must be an integer or float")
    return value ** 2

