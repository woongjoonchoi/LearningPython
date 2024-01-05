X = 40

def f1():
    X = 20
    
    def f2():
        print(X)
        
    return f2

a= f1()

a()