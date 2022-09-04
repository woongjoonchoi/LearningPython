def maker(N) :
    state= 1
    def action(X) :
        d = state
        print(d)
        return X**N
    return action

f=maker(2)

print(f)

print(f(3))
print(f(4))

g = maker((3))


print(g(3))
print(g(4))


