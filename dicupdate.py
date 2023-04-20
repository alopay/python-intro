person = {}

person["first_name"] = "Alopay"
person['last_name'] = "Developer"
person["age"] = 50

person["number_of_children"] = 4

person['children'] = ["boy1", 'boy2', 'girl1', 'girl2']

person["pets"] = {'cats': "Cat1", "dog": "dog1"}

favorites = {
  'food': "Amala and Ewedu",
}

favorites['fruits'] = "Orange"

favorites['sport'] = "Football"

print(person)

print("\n")

# .update() is used to merge 2 dictionaries

person.update(favorites)

print(person)

person.update(complexion="Dark Skinned")

print("\n")
print(person)

person.update([('car', "Tesla"), ("address", "UK")])

print(person)
