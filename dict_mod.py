person = {}


person["first_name"] = "Alopay"
person['last_name'] = "Developer"
person["age"] = 50


person["number_of_children"] = 4

person['children'] = ["boy1", 'boy2', 'girl1', 'girl2']

person["pets"] = {'cats': "Cat1", "dog": "dog1"} 
# print(person)

# print(person['children'])
# print(person['children'][-1])

# print(person["pets"])
# print(person["pets"]['cats'])

person[True] = "is_married"
# print(person)


person1 = {
  'pet': "Dog",
  'pet': "Cat",
  'pet': "Goat",
  "animal": "Goat"
}

print(person1['animal'] == person1['pet'])

# if you specify a key a second time during the initial creation of a dictionary, the second occurrence will override the first
# it can store the multiples values that are identical

# print(person1)

# fruits {
#   ['veggies', 'tomato'] : "Carrot",
#   ['pawpaw', 'banana'] : "Coconut",
# }
# dict can't take list as keys

fruits = {
  (1, 2): "Banana",
  (2, 2): "PawPaw",
  (1, 3): "Mango"
}
# print(fruits)

# we use in operator to check if a key is present in our dictionary

print("first_name" in person)
print("children" not in person)



print(len(person))
print(person.clear())

print(person)

