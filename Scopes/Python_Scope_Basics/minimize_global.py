X = 99


def a():
    global X
    X = 32
def b() :
    global X
    X= 56
    
# Q .what is value of X?
# A. It 's dependent on what you calledd

b()
print((X))