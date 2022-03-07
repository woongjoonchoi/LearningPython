S = 'A\nB\tC'
# \n is end-of-line , \t is tab character
# Each stands for just one character


print(len(S))
print(S)
print(ord('\n'))
# \n is a byte with the binary value 10 in ASCII


S= 'A\0B\0C'

# \0 ,  binary zero byte, does not terminate string
print(len(S))
print(S)