""" Project Euler
    Problem 38
    Pandigital Multiples """


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

def main():
    gPM = 0
    for i in range(1000,10000):
        curPM = ''
        for j in range(1,100):
            curPM += str(i*j)
            #print curPM
            if len(curPM) > 9:
                break
            elif isPandigital(curPM):
                if int(curPM) > gPM:
                    gPM = int(curPM)
    return gPM

if __name__ == "__main__":
    main()
