# Nested List
# index on nested list
# slicing on nested

domestic_animal = ["Cat", "Dog", "Bird"]
# print(domestic_animal)
# domestic_animal[0] = "Meow"
print(domestic_animal)
wild_animal = ["Elephant", "Lion", "Zebra"]
animal = ["Hyena", "Ant", "Baboon", domestic_animal, wild_animal]

print(animal[2])
print(animal[4])

print(animal[-1][-1])

print(animal[-2][:2])

animal[-2][-1] = "Goat"

print(animal)