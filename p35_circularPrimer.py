""" Project Euler
    Problem 35
    Circular Primer """

""" The number, 197, is called a circular prime because all
    rotations of the digits: 197, 971, and 719, are themselves prime.
    There are thirteen such primes below 100:

    2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.

    How many circular primes are there below one million? """

from itertools import permutations

def rotate(n):
    """ Rotates a number.
        rotate :: int -> str """
    
    a = str(n)
    yield a
    for i in range(len(a)):
        a = a[1:]+a[0]
        yield a

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

def findCircPrimes(n):
    """ findCircPrimes :: int -> int
        Finds the number of circular primes below a number n. """
    
    #Starting at 3 allows the loop to
    #   run faster by incrementing by two
    primesSoFar = [2]

    #Count up by two until reaching the squareroot of the number.
    for i in range(3, n, 2):
        if i in primesSoFar:
            continue
        curPerms = []
        isCirc = 1
        for perm in rotate(str(i)):
            number = int(''.join(perm))
            if not isPrime(number):
                isCirc = 0
                break
            if number in curPerms:
                continue
            curPerms.append(number)
        if isCirc:
            primesSoFar += curPerms
    #Debugging statement
    #print primesSoFar
    return len(primesSoFar)
        

print findCircPrimes(10**6)

    
