# Paste your code into this box
s = 'azcbobobegghakl'

count = 0

for ltr in s:
     if ltr in ['a', 'e', 'i', 'o', 'u']:
         count += 1
print 'Number of vowels: %s' % count
