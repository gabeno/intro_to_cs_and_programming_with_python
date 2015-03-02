# Bisection search
# Create a program that guesses a secret number


def guess_number():
    print 'Please think of a number between 0 and 100!'
    high = 100
    low = 0
    guessed = False

    while not guessed:
        guess = (high + low) / 2
        print 'Is your secret number %s?' % guess
        user_fdbck = raw_input('Enter "h" to indicate the guess is too high. \
                                Enter "l" to indicate the guess is too high. \
                                Enter "c" to indicate I guessed correctly. ')

        if user_fdbck == 'l':
            low = guess
        elif user_fdbck == 'h':
            high = guess
        elif user_fdbck == 'c':
            guessed = True
        else:
            print 'Sorry, I did not understand your input.'

    print 'Game over.Your secret number was: %s' % guess


if __name__ == '__main__':
    guess_number()
