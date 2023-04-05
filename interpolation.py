# string interpolation

n = 20
t = 3

product = n * t

print(product)

print("The product of", n, "and", t, "is", product)
statement = f"The product of {n} and {t} is {product}" 
print(statement)

"""
  This is an example of string interpolation
"""

sound = "Woo"
number = 3
animal = "dog"
sentence = f"The {animal} barks {sound} {number} times"

print(sentence)
