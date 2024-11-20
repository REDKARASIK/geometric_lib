import math
#add for test
'''
Import module math that keeps math constants and formulas
'''

def area(r):
    '''
    Function get r radius of circle and return 2 * math.pi(3,14) * r^2
        - area
    Example: area(10) = 3,14 * 10 * 10
    '''
    return math.pi * r * r


def perimeter(r):
    '''
    Function get r radius and return 2 * math.pi(3,14) * r
        - perimeter of circle

    Example: perimeter(10) = 20 * 3,14
    '''
    return 2 * math.pi * r

