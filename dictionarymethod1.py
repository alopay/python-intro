person = {}


person["first_name"] = "Alopay"
person['last_name'] = "Developer"
person["age"] = 50


person["number_of_children"] = 4

person['children'] = ["boy1", 'boy2', 'girl1', 'girl2']

person["pets"] = {'cats': "Cat1", "dog": "dog1"} 
# print(person)

print(person['pets'])

print(person.get("pets"))

# print(person['perry'])

# it returns None by default when the key isn't available
print(person.get("perry"))

# If <key> is not found and the optional <default> argument is specified, that value is returned instead of None

print(person.get('perry', [1, "test me", True, {"hello": "greetings"}]))


