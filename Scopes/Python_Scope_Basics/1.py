#Global Variables
X =99

def func(Y) :
    # Z : Local scope
    # X :global
    # Y : local
    Z = X+Y
    return Z

print(func(1))