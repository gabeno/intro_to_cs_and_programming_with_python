# Find the cube root of a number x


def guess_cube_root():
    '''take a number x, and get its cube root
    through a number of guesses
    '''

    x = int(raw_input('Please enter an integer: '))
    for ans in range(0, abs(x) + 1):
        if ans**3 == abs(x):
            break

    if ans**3 != abs(x):
        print '%s is not a perfect cube!' % x
    else:
        if x < 0:
            ans = -ans
        print 'cube root of %s is %s' % (x, ans)

if __name__ == '__main__':
    guess_cube_root()
