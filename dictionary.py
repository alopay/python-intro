# list, tuples, dictionary

# {} is the symbol of a dictionary
# dictionaries are mutables. 
# it can be dynamic. it can shrink or expand
# dictionary can be nested

pry1 = {
 "key": "value"
}

# the key is always on the left side, while the value is on the right side
premier_league = ["chelsea", "manu", "ars"]
premier_league.append("Tot")
# print(premier_league)

premier_league_team = {
  "London": "Chelsea",
  "North London": "Arsenal",
  "Manchester": "Manchester United"
}

premier_league_team["Wales"] = "Cardiff"

# print(premier_league_team)

# print(premier_league_team["London"])

classes = {
  1 : "Baby",
  2 : "Kids",
  3 : "Boys"
}

# append can't be used for dictionaries same as our index position
# classes.append("Toys")

classes[0] = "Toddler"

# print(classes)
# print(premier_league_team[0])


person = {}

print(person)

person["first_name"] = "Alopay"
person['last_name'] = "Developer"
person["age"] = 50

print(person)

person["number_of_children"] = 4
print(person)

person['children'] = ["boy1", 'boy2', 'girl1', 'girl2']

person["pets"] = {'cats': "Cat1", "dog": "dog1"} 
print(person)

