'''
Write a procedure called oddTuples, which takes a tuple as input, and returns
a new tuple as output, where every other element of the input tuple is copied,
starting with the first one. So if test is the tuple
('I', 'am', 'a', 'test', 'tuple'), then evaluating oddTuples on this input
would return the tuple ('I', 'a', 'tuple').
'''


def oddTuples(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Your Code Here
    newTup = ()
    for idx, val in enumerate(aTup):
        if idx % 2 == 0:
            newTup = newTup + (val, )
    return newTup


def oddTuples1(aTup):
    '''
    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # a placeholder to gather our response
    rTup = ()
    index = 0

    # Idea: Iterate over the elements in aTup, counting by 2
    #  (every other element) and adding that element to
    #  the result
    while index < len(aTup):
        rTup += (aTup[index],)
        index += 2

    return rTup


def oddTuples2(aTup):
    '''
    Another way to solve the problem.

    aTup: a tuple

    returns: tuple, every other element of aTup.
    '''
    # Here is another solution to the problem that uses tuple
    #  slicing by 2 to achieve the same result
    return aTup[::2]


def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    # Your Code Here
    biggest = 0
    for i in aDict:
        biggest = max(biggest, len(aDict[i]))

    for i in aDict:
        if len(aDict[i]) == biggest:
            return i


def biggest1(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    result = None
    biggestValue = 0
    for key in aDict.keys():
        if len(aDict[key]) >= biggestValue:
            result = key
            biggestValue = len(aDict[key])
    return result


if __name__ == '__main__':
    # aTup = ('I', 'am', 'a', 'test', 'tuple')
    # print oddTuples(aTup)
    animals = {'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}
    animals['d'] = ['donkey']
    animals['d'].append('dog')
    animals['d'].append('dingo')
    print biggest(animals)
