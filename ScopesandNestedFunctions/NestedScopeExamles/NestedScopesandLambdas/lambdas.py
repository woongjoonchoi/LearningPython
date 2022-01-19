def func() :
    x = 4
    action = (lambda n : x **n) # x rememeberd , x from enclosing def
    return action


f  = func()

print(f(2)) 

def func() :
    x = 4
    action = (lambda n , x=x: x **n)  # x passed as default argument value
    return action

f  = func()

print(f(2))