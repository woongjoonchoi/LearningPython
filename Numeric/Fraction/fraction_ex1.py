from fractions import Fraction

a= Fraction(1,3)

print(a)

print(Fraction('.5'))


print((2.5).as_integer_ratio())

f = 2.5

print(Fraction(*f.as_integer_ratio()))

z = Fraction(*f.as_integer_ratio())

x = Fraction(1,3)

print(x+z)

print(float(x)) # Convert Fraction to float


print(Fraction.from_float(1.75))