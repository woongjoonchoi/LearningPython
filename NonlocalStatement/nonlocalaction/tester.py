def tester(start) :
    state =start
    def nested(label) :
        print(label , state)
    return nested

F = tester(0) 

# print(F('spam')) 
F('spam')

F('ham')


def tester(start) :
    state = start
    def nested(label) :
        nonlocal state
        print(label , state)
        state +=1 
        
    return nested

F = tester(0)

F('spam')

F('ham')

G = tester(42)

G('spam')

G('egss')


F('bacon')

# print(F('ham'))


