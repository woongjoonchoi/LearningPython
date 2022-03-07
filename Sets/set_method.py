x= set('abced')
y= set('hello')


z = x.intersection(y)
print(z)

z.add('SPAM')

print(z)

z.update(set(['ac','bc']))
print(z)

z.update('jkl')
print(z)

z.remove('bc')

print(z)

for item in "cdf" :
    print(item * 3 )