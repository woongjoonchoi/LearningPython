def f1() :
    X = 88
    def f2(X=X) :
        print(X)
    f2()


f1()

def f1() :
    X = 88
    f2(X)  # Forward Reference okay

def f2(X) :
    print(X)
    
f1()