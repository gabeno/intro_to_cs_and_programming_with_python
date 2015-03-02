# Write a program that asks the user to input 10 integers,
# and then prints the largest odd number that was entered.
# If no odd number was entered, it should print a message
# to that effect


def get_int(count):
    '''get count number of integers from a user'''

    num_list = []
    raw_input('Please give me %s integers. Press ENTER when ready...' % count)
    for i in range(1, count + 1):
        user_input = int(raw_input('%s: ' % i))
        num_list.append(user_input)

    return num_list


def check_odd_num(num_list):
    '''select largest odd number in list and return it
    or return appropriate message
    '''
    odd_list = [i for i in num_list if i % 2 != 0]
    if len(odd_list):
        print 'the largest odd number you entered is %s' % max(odd_list)
    else:
        print 'No odd number found!'

if __name__ == '__main__':
    num_list = get_int(10)
    check_odd_num(num_list)
