import math as m

# PYTHAGOREAN THEOREM ON A RIGHT TRIANGLE / RECTANGLE:
print("RIGHT TRIANGLE / RECTANGLE")

a = float(input("Catheter a: "))            # c = √a²+b²
b = float(input("Catheter b: "))
c = m.sqrt(a**2 + b**2)

print(c)

# PYTHAGOREAN THEOREM ON A SQUARE:
print("SQUARE")

a = float(input("Sides a: "))               # c = √a²+a²
c = a * m.sqrt(2)
print(c)

# PYTHAGOREAN THEOREM ON A TRAPEZOID:   
print("TRAPEZOID")

a = float(input("Base a: "))
b = float(input("Base b: "))                # c = √(a+b)²+h²
h = float(input("Height h: "))

c = m.sqrt((a+b)**2+h**2) 
print(c)

#PYTHAGOREAN THEOREM ON A PARALLELOGRAM:
print("PARALLELOGRAM")

b = float(input("Base b: "))                # c = √b²+h²
h = float(input("Height h: "))
d = m.sqrt(b**2+h**2)
print(d)