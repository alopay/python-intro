# tuples

# tuples are like list 
# tuples use () instead of []
# tuples are immutable

names = ['Ola', "Ade", "Chichi"]
# print(names)
names[2] = "Tobi" # we can change the value of an item in a list

# print(names)

# tuples cannot be changed

# age[1] = 14 we can't change the value of an item in a tuple
# print(age)

# print(age[::-1])


# str(), float(), bool()

number = 32
# print(type(number))
# number = str(number)

# print(type(number))
age = ("22", 13, True)
print(age)


# print(type(age))

age = list(age)
age[1] = 12
age = tuple(age)

info = (20, 2.2, True, "Bola", [2, 3, 4])
print(info[-1][1])
print(age)
# print(type(age))

# conclusion

"""
1. List and tuples are ordered
2. they can contain any data type
3. They can be accessed by index
4. they can be nested
5. list are mutable (can be changed), tuples aren't mutable (cannot be changed)
"""