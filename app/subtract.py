def subtract(num1, num2):
    if type(num1) is not int or type(num2) is not int:
        raise TypeError
    difference = num1 - num2
    return difference
