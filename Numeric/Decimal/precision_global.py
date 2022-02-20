from decimal import Decimal

import decimal
decimal.getcontext().prec = 2 
# decimal.getcontext().prec = 4 

print(Decimal(1) / Decimal(3) + 4)


print(1999+0.1333)

decimal.getcontext().prec = 6


print(Decimal(1999+.13445)+Decimal(4))

print(Decimal(str(1999+1.444544)))

print(float(str(1999+1.444544)))