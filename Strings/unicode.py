from sys import getsizeof

print('sp\xc4m')


print(u'sp\xc4m' )
print( b'a\x01c' )


print('spam')
print(getsizeof('spam'))

print('spam'.encode('utf8'))

print(getsizeof('spam'.encode('utf8')))

print('spam'.encode('utf16'))

print(getsizeof('spam'.encode('utf16')))