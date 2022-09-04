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


def new_tester(start) :
    def nested(label) :
        print(label , state[0])
        state[0] += 1
    state = [start]
    return nested

FF = new_tester(0)

FF('dd')

FF('dd')
# print(F.state)