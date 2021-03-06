""" Project Euler
    Problem 49
    Prime permutations """

""" The arithmetic sequence, 1487, 4817, 8147, in which
    each of the terms increases by 3330, is unusual in two ways:
    (i) each of the three terms are prime, and,
    (ii) each of the 4-digit numbers are permutations of one another.
    There are no arithmetic sequences made up of
    three 1-, 2-, or 3-digit primes, exhibiting this property,
    but there is one other 4-digit increasing sequence.

    What 12-digit number do you form by concatenating
    the three terms in this sequence? """

from itertools import permutations

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

def main():
    """ Iterates through all 4-digit numbers
        checks a list of all permutations of the primes it finds
        and looks for an arithmetic sequence in that list. """
    
    unusualPrimes = []
    #We only care about 4-digit numbers.
    for i in range(1000,10000):

        #We only care about primes.
        if isPrime(i):
            somePerms = []
            for perm in permutations(str(i)):
                num = int(''.join(perm))

                #Add permutations that are prime to a temp list.
                #Avoid duplicates or primes we have already found in the main loop.
                if isPrime(num) and not num in somePerms and num >= i:
                    somePerms.append(num)
            #The sequence will be at least length 3.
            if len(somePerms) > 2:

                #Look through the list to see if there is an arithmetic sequence.
                firstPrime = somePerms[0]
                for j in range(1,len(somePerms)):
                    difference = somePerms[j] - firstPrime
                    possibleNextPrime = difference + somePerms[j]
                    if possibleNextPrime in somePerms:
                        unusualPrimes.append(\
                            [firstPrime, somePerms[j], possibleNextPrime])
                                       
                #print somePerms
    for arithmeticSeq in unusualPrimes:
        print ''.join(["%s" % prime for prime in arithmeticSeq])


        
if __name__  == "__main__":
    main()
    
