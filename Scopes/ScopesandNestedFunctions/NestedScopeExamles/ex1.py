X = 99

def f1():
    X = 88
    Y= 1234
    def f2(X = X):
        X +=1
        Y +=4
        print(X)
    f2()
    print(X)
f1()