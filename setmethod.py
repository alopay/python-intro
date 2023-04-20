# sets is {}

# sets cannot be ordered
# sets are unique

# bool values are represented as 1 and 0. True means 1, False means 0.

numbers = {1, 0, "testme", "Try me", True, 3, 4, 5, 7, False}

print(numbers)
print(numbers)


number2 = {12, 0, 19, 22, 300, 1, 1}
number3 = [12, 0, 19, 22, 300, 1, 1]
print(number2)
print(number3)

brands = {'pepsi', 'kfc', 'amazon', 'jumia', 'konga'}
brand2 = {'coca cola', 'facebook', 'pepsi'}
print(brands)


# Set Operators

# print(len(brands))

# print("pepsis" not in brands)

# .union() method is used to merge 2 sets together temporarily


# print(brands|brand2)



a = {1, 2, 3, 4}
b = {2, 3, 4, 5}
c = {3, 4, 5, 6}
d = {4, 5, 6, 7}

all_brands = brands.union(brand2)
print(a.union(b, c, d))

alp = a.union(b, c, d)

print(all_brands)
print(alp)


brands.add("google")


# brands.remove('pepsi')


# brands.discard('konga') # discard serves the same purpose as remove

print(brands)


brands.pop() # Removes a random element from a set.

print(brands)
print(all_brands)

all_brands.pop()

print(all_brands)

brands.clear()

print(brands)