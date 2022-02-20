def tester(start) :
    state = start
    def nested(label) :
        nonlocal state
        print(label , state)
        state +=1 
        
    return nested

F= tester(0)

# F.state+=1
print(F('egg'))

print(F('bana'))
# print(F.state)