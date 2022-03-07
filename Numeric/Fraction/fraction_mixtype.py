from fractions import Fraction

x = Fraction(1,3)

print(x+2)  # Fraction + int -> Fraction

print(x+2.0)  # Fraction+ float - > float

print(x + Fraction(3,4)) # Fraction + Fraction -> Fraction p