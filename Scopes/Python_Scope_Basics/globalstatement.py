X = 88

def C() :
    global X
    X = 999

    print(X)
C()
print(X)


y,z = 1,2
def all_global() :
    global x   # x scope is global ,
    x = y+z  # y,z scope is global too
all_global()
print(x)