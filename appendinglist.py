# modifying lists

# "+=" to append to a list

# appending list
name = "Hakeem"

name += " Olamide"

age = 3

age += 1
print(age)
age += 6
print(age)

age -= 5

print(age)

print(name)

# we can't append to a variable name that doesn't exist
# school += "My School"
fruits = ['orange', 'cucumber', 'date', 'banana']

# print(type(fruits[-2]))

fruits += ['strawberry', 'cherry', 'coconut']

print(fruits)

fruits[1] = []

print(fruits)