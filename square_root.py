# Find the square root of a number, x
# start with a guess g
# square it and check if it is close enough to x
# if not, make a new guess by averaging x and x/g, then repeat
# if yes, it must be the square root!

import random


def guess_square_root():
    '''Find the square root of a number'''

    x = float(raw_input('Please give me an integer: '))
    g = random.randint(1, int(x) / 4)
    epsilon = 0.001

    while (abs(g*g - x) > epsilon):
        g = 0.5 * (g + x/g)

    print 'Square root of %s is %s' % (x, g)


if __name__ == '__main__':
    guess_square_root()
