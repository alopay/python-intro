# sets


age = {1, 'tade', False}

age.add(45)
print(age)

numbers = {1, 0, 5, 3, 2, 1}

print(numbers)


# frozenset 
# sets are mutable while frozensets are immutable

ages = frozenset([32, 12, 19])
ages.add(11)
print(ages)

print(len(ages))