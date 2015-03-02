# Write a program that asks the user to enter an integer and
# prints two integers, root and pwr , such that 0 < pwr < 6
# and root**pwr is equal to the integer entered by the user.
# If no such pair of integers exists, it should
# print a message to that effect.


def check_root_pwr():
    user_int = int(raw_input('Please enter an integer: '))
    root = 0
    for pwr in range(7):
        root**pwr
        root += 1

    if root**pwr != abs(user_int):
        print 'Not lucky!'
    else:
        print 'root: %s' % root,
        print 'pwr %s' % pwr

if __name__ == '__main__':
    check_root_pwr()
