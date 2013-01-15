""" Project Euler
    Problem 41
    Pandigital Multiples """

from itertools import permutations

def isPandigital(*args):
    """ *int -> bool
        returns true if the the concatenated args
            identity is pandigital """
    number = ''
    for n in args:
        number += str(n)
    number = sorted(number)
    compareList = [str(x) for x in range(1,len(number)+1)]
    return compareList == number

def isPrime(n):
    """ isPrime :: int -> bool
        Determines is a number is prime."""
    if n < 2 or n % 2 == 0:
        return False
    if n == 2 or n == 3:
        return True
        
    #Count up by two until reaching the squareroot of the number.
    for i in range(3, int(n**0.5)+1, 2):
        if n % i == 0:
            return False
    return True

#Brute force search forthe largest prime
##largest = 1
##for i in xrange(1,987654322):
##    if isPandigital(i) and isPrime(i) and i > largest:
##        largest = i
##        print "The largest pandigital so far is", largest
        
#This method searchs using permutations of n-length pandigitals
##largest = 1
##pandigitalList = [str(x) for x in range(1,10)]
##for i in range(10,2,-1):
##    for perm in permutations(pandigitalList[:i]):
##        number = int(''.join(perm))
##        print number 
##        if isPrime(number) and number > largest:
##            largest = number
            
print largest
