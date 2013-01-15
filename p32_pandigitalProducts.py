""" Project Euler
    Problem 32
    Pandigital Products """

def isPandigital(*args):
    """ *int -> bool
        returns true if the the concatenated args
            identity is 1 through 9 pandigital """
    number = ''
    for n in args:
        number += str(n)
        if len(number) > 9:
            return False
    if len(number) < 9:
        return False
    number = sorted(number)
    compareList = [str(x) for x in range(1,10)]
    return compareList == number

def findSumPandigitals():
    """ None -> int
        Computes the sum of the roducts whose multiplicand/multiplier/product
            identity can be written as a 1 through 9 pandigital.
            HINT: Some products can be obtained in more than one
            way so be sure to only include it once in your sum."""
    
    """ To find the boundary conditions, calculate the maximum multiplier
            given the multiplicand and the fact that the maximum number
            of digits from all numbers must be 9 """
    products = []
    for i in xrange(1,100):
        if (i < 10):
            for j in xrange(100, 4988):
                prod = i*j
                if isPandigital(i,j, prod) and prod not in products:
                    products.append(prod)
        else:
            for j in xrange(100,988):
                prod = i*j
                if isPandigital(i,j, prod) and prod not in products:
                    products.append(prod)
    return sum(products)
    
    
