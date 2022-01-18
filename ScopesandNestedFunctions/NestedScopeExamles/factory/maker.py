def maker(N) :
    def action(X) :
        return X**N
    return action

f=maker(2)

print(f)