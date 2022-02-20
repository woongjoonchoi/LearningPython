def makeActions() :
    acts=[]
    for i in range(5): # Tries to remember each i
        acts.append(lambda x : i ** x) # But all remember same last i
        
    return acts

acts = makeActions()


print(acts[0])


print(acts[0](2))
print(acts[1](2))
print((acts[4](2)))

print('--------------------')

def makeActions() :
    acts=[]
    for i in range(5) :  # Diffenreec . Use default i
        acts.append(lambda x , i = i : i**x) 
        
    return acts

acts  =  makeActions()

print(acts[0](2))

print(acts[2](2))

print(acts[4](2))


print('--------------------')

def makeActions() :
    acts=[]
    for i in range(5) :  # Diffenreec . Use default i
        def temp(x) :
            return i **x
        acts.append(temp) 
        
    return acts

acts  =  makeActions()

print(acts[0](2))

print(acts[2](2))

print(acts[4](2))