def f1() :
    X = 88
    def f2() :
        print(X) 
    return f2

action = f1()
action()