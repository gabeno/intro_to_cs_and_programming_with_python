'''
Suppose you are given two strings (they may be empty), s1 and s2.
You would like to "lace" these strings together, by successively
alternating elements of each string (starting with the first character of s1).
If one string is longer than the other, then the remaining elements of the longer
string should simply be added at the end of the new string. For example,
if we lace 'abcd' and 'efghi', we would get the new string: 'aebfcgdhi'.

Write an iterative procedure, called laceStrings(s1, s2) that does this.
'''
def laceStrings(s1, s2):
    """
    s1 and s2 are strings.

    Returns a new str with elements of s1 and s2 interlaced,
    beginning with s1. If strings are not of same length,
    then the extra elements should appear at the end.
    """
    # Your Code Here
    new_str = ''

    str_len = min(len(s1), len(s2))

    if not str_len:
        return new_str

    count = 0

    while count < str_len:
        new_str += s1[count]
        new_str += s2[count]
        count += 1

    if len(s1[count:]):
        new_str += s1[count:]

    if len(s2[count:]):
        new_str += s2[count:]
    return new_str


if __name__ == '__main__':
    print laceStrings('', '')
    print laceStrings('abcd', 'efghi')
    print laceStrings('gabriel', 'abeno')
