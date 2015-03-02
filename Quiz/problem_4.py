'''
Write a simple procedure, myLog(x, b), that computes the logarithm
of a number x relative to a base b. For example, if x = 16 and b = 2,
then the result is 4 - because 2^4=16. If x = 15 and b = 3,
then the result is 2 - because 3^2 is the largest power of 3
less than 15.

In other words, myLog should return the largest power of b such
that b to that power is still less than or equal to x.

x and b are both positive integers; b is an integer greater than or
equal to 2. Your function should return an integer answer.

Do not use Python's log functions; instead, please use an iterative
or recursive solution to this problem that uses simple arithmetic
operators and conditional testing.
'''
def myLog(x, b):
    '''
    x: a positive integer
    b: a positive integer; b >= 2

    returns: log_b(x), or, the logarithm of x relative to a base b.
    '''
    # Your Code Here
    num = 0
    power = 0
    while True:
        power = num
        num += 1
        if b**num > x:
            break
        print b**power, power, x

    return power

if __name__ == '__main__':
    print myLog(15, 3)
