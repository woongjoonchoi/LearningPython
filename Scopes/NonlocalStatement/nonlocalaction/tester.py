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



def new_tester(start) :
    state = 2
    def nested(label) :
        # nonlocal state
        nonlocal state
        d = state
        print(label , state)
        # state +=1  # assign이 들어가면 자동으로 local취급이 되는듯 functio에서
        
    return nested
dd = new_tester
new_test = dd(0)

print('new_test')
new_test('ss')

new_test('sse')

# print(new_test.state)
# print(dir(new_test))
def maker(N) :
    state= 1
    def action(X) :
        d = state
        print(d)
        return X**N
    return action



