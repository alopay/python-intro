person = {}


person["first_name"] = "Alopay"
person['last_name'] = "Developer"
person["age"] = 50


person["number_of_children"] = 4

person['children'] = ["boy1", 'boy2', 'girl1', 'girl2']

person["pets"] = {'cats': "Cat1", "dog": "dog1"} 
# print(person)

# .items() method

# print(person)
# print(person.items())

# print("\n")
# .items() is used to Return a list of key-value pairs in a dictionary.

# print(person.keys())
# Returns a list of keys in a dictionary.


# print(person.values())
# Returns a list of values in a dictionary.

print(f'{person} is the dict')
print(f'{len(person)} is the total value present in our dictionary')
print("\n")

total_children = person.pop("number_of_children", 12)

print("\n")
last_item = person.popitem()

person.popitem()

print(f'{person} is the remaining dictionary after removal')
print(last_item)

print(total_children)

print(f'{len(person)} is the total value present in our dictionary')
print("\n")
