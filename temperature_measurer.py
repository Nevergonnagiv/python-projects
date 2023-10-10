# CELSIUS TO FAHRENHEIT:

a = float(input("Celsius: "))
c = (a * 1.8) + 32
print(str(c) + " Fahrenheit")

# FAHRENHEIT TO CELSIUS:

a = float(input("Fahrenheit: "))
c = (a - 32) / 1.8
print(str(c) + " Celsius")

# CELSIUS TO KELVIN:

a = float(input("Celsius: "))
c = a + 273.15
print(str(c) + " Kelvin")

# FAHRENHEIT TO KELVIN:

a = float(input("Fahrenheit: "))
c = (a - 32) / 1.8 + 273.15
print(str(c) + " Kelvin")

# KELVIN TO CELSIUS: 

a = float(input("Kelvin: "))
c = a - 273.15
print(str(c) + " Celsius")

# KELVIN TO FAHRENHEIT

a = float(input("Kelvin: "))
c = (a - 273.15) * 1.8 + 32
print(str(c) + " Fahrenheit")