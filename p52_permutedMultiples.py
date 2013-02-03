""" Project Euler
    Problem 52
    Andrew Roetker """

""" It can be seen that the number, 125874, and its double,
    251748, contain exactly the same digits, but in a different order.

    Find the smallest positive integer, x,
    such that 2x, 3x, 4x, 5x, and 6x, contain the same digits."""

from itertools import permutations

def hasSameDigits(*args):
    """Checks if the arguements have the same digits and or characters."""
    
    a = sorted(str(args[0]))
    for arg in args:
        b = sorted(str(arg))
        if a != b:
            return False
    return True


def main():
    """Only check the ranges where 6 times the number is the same length."""
    
    ranges = [(10,17),(100,170),(1000,1700),(10000,17000), (100000,170000), (1000000,1700000)]
    for rAnge in ranges:
        lower, upper = rAnge
        for i in range(lower, upper):
            if hasSameDigits(i,2*i, 3*i, 4*i, 5*i, 6*i):
                return i

if __name__ == "__main__":
    print main()
