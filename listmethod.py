# lists methods

# "+=" to append to a list

# we can't append to a variable name that doesn't exist
# school += "My School"
fruits = ['orange', 'cucumber', 'date', 'banana']

print(fruits)

# .append() method also functions like '+='
# unlike '+=' append can only take one argument
# append can nest another list inside our list
# append adds new item at the end of the list
fruits.append("strawberry")
vegetables = ['Onion', "Pepper"]
fruits.append(vegetables)

fruits += ["almond", 'coconut']

print(fruits)

# removing from a list
# .remove()
# it also takes one argument only
fruits.remove("cucumber")
print(fruits)
# fruits.append('cucumber')
# print(fruits)

# .insert() method
# .insert() add based on the index position specified
# first argument is the index destination
# second argument is the item to be added to the index position
fruits.insert(0, 'cucumber')

print(fruits)

# .extend() method extends the list
# it takes only list
# to avoid breaking our code. we use list in extend method
# += and extends method serve the same purpose
fruits.extend(['apple', 'grape'])
# fruits.extend(["try"])
# fruits += "test"
print(fruits)
