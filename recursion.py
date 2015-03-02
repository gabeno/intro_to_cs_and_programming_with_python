def iterPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here

    num = 1
    while exp > 0:
        num *= base
        exp -= 1

    return num


def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Your code here
    if exp <= 0:
        return 1
    return base * recurPower(base, exp - 1)


def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    # Your code here
    if exp % 2 != 0 and exp > 0:
        return base * recurPowerNew(base, exp - 1)
    elif exp > 0 and exp % 2 == 0:
        return recurPowerNew(base * base, exp / 2)
    elif exp <= 0:
        return 1


def gcdIter(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    test_value = min(a, b)
    while a % test_value != 0 or b % test_value != 0:
        test_value -= 1
    return test_value


'''
A clever mathematical trick (due to Euclid) makes it easy to find
greatest common divisors. Suppose that a and b are two positive integers:

    If b = 0, then the answer is a
    Otherwise, gcd(a, b) is the same as gcd(b, a % b)

Ref: https://en.wikipedia.org/wiki/Euclidean_algorithm#Worked_example
'''
def gcdRecur(a, b):
    '''
    a, b: positive integers

    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    if b == 0:
        return a
    return gcdRecur(b, a % b)


def lenRecur(aStr):
    '''
    aStr: a string

    returns: int, the length of aStr
    '''
    # Your code here
    if aStr == '':
        return 0
    else:
        return 1 + lenRecur(aStr[1:])


'''
Base Case:
==========
You should be thinking about 3 situations:
    What happens when the string is empty?
    What happens when the string is of length 1?
    What happens when the test character equals the middle character?

Recursive Case:
===============
You should be thinking about 2 situations:
    What happens when the test character is smaller than the middle character?
    What happens when it is larger?
'''


def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string

    returns: True if char is in aStr; False otherwise
    '''
    # Your code here
    if aStr == '':
        return False

    if len(aStr) == 1:
        if aStr == char:
            return True
        else:
            return False
    else:
        idx = len(aStr) / 2
        g = aStr[idx]
        if g > char:
            return isIn(char, aStr[:idx])
        elif g < char:
            return isIn(char, aStr[idx:])
        elif g == char:
            return True


def semordnilapWrapper(str1, str2):
    # A single-length string cannot be semordnilap
    if len(str1) == 1 or len(str2) == 1:
        return False

    # Equal strings cannot be semordnilap
    if str1 == str2:
        return False

    return semordnilap(str1, str2)


def semordnilap(str1, str2):
    '''
    str1: a string
    str2: a string

    returns: True if str1 and str2 are semordnilap;
            False otherwise.
    '''
    # Your code here
    if len(str1) != len(str2):
        return False

    if len(str1) == 1:
        return str1 == str2

    if str1[0] == str2[-1]:
        return semordnilap(str1[1:], str2[:-1])
    else:
        return False

if __name__ == '__main__':
    print semordnilapWrapper('a', 'a')
    print semordnilapWrapper('gaaa', 'gaaa')
    print semordnilapWrapper('live', 'evil')
