from fractions import Fraction

print(4.0/3)


print((4.0/3).as_integer_ratio())  


x = Fraction(1,3)

a = x + Fraction(*(4.0/3).as_integer_ratio())

print(a)

print(22517998136852479/13510798882111488)
# print(a[1]/a[0])

print(f"a limit denominator : {a.limit_denominator(100)}")




y = 1/7

print(y.as_integer_ratio())

print(2573485501354569/18014398509481984)