# Convert Example Learning Python


# Example 1
'''
>>> x = 1234
>>> res = 'integers: ...%d...%−6d...%06d' % (x, x, x)
>>> res
'integers: ...1234...1234 ...001234'
'''

x = 1234

res = f'integers:...{x}...{x:<6}...{x:06}'
print(res)


# Example 2

'''
>>> x = 1.23456789
>>> x # Shows more digits before 2.7 and 3.1
1.23456789
>>> '%e | %f | %g' % (x, x, x)
'1.234568e+00 | 1.234568 | 1.23457'
>>> '%E' % x
'1.234568E+00'
'''

x= 1.23456789

res  = f'{x:e} | {x:f} | {x:g}'

print(res)

res = f'{x:E}'

print(res)

# Example 3

'''
>>> '%f, %.2f, %.*f' % (1/3.0, 1/3.0, 4, 1/3.0)
'0.333333, 0.33, 0.3333'
'''
x=4

print(f'{1/3.0:f}, {1/3.0:.2} , {1/3.0:.{x}}')

# print('%f, %.2f, %.*f' % (1/3.0, 1/3.0, x, 1/3.0))