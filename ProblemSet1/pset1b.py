# Paste your code into this box
s = 'azcbobobegghakl'

count, num = 0, 0

for ltr in s:
    if ltr == 'b' and s[count: count + 3] == 'bob':
        num += 1
    count += 1

print num
