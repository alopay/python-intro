# Strings in Python
# Strings are always represented by '' or ""

introduction = "I am Alopay"
# print(introduction)
learning_path = "I am a Beginner Python Developer"
# print(learning_path)

# print(introduction, learning_path)

# String Concatenation
s = "foo"
t = "bar"
z = "baz"


r = "Alo"
x = "pay"
print(r+x) # expected result will be 'Alopay'

print("Go Team"+"!!!") 


greet = "Hello "
print(greet*3) # expected result will be "Hello" in 3 places

letter = "w"

print(letter in greet) # return a boolean value. it is False

new_letter = "H"
print(new_letter in greet) # return a boolean value. it is True

print(letter not in greet) # return a boolean value. it is True

print(new_letter not in greet) # return a boolean value. it is False
