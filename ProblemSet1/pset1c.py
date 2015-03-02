s = 'zyxwvutsrqponmlkjihgfedcba'

count = 1
l = []
new_str = ''

for ltr in s:
    if count < len(s):
        if not s[count - 1] > s[count]:
            new_str = new_str[:-1]
            new_str =  new_str + s[count - 1] + s[count]
        else:
            new_str = ''
        print s[count - 1], s[count]
    l.append(new_str)
    count += 1

print l
d = {}
for w in l:
    d.setdefault(len(w), w)

print d[max(d.keys())] or s[0]
