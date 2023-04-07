# Character Classification in strings

name = "Bello AbdulHakeem"
name1 = "Alopay123"
name2 = "Alopay"
age = "123"
# isalnum() is used to check if the targetted string has numeric and alphabetic values. It usually returns True/False

# print(name.isalnum())
# print(name1.isalnum())

# isalpha() is used to check if the targetted string has alphabetic value only.
# It usually returns True/False
# print(name.isalpha())
# print(name1.isalpha())
# print(name2.isalpha())

# isdigit() is used to check if the targetted string has numeric value only.
# It usually returns True/False
# print(name1.isdigit())
# print(age.isdigit())

new_name = name.lower()
# print(new_name)
# print(name)

# print(name.islower())
# print(new_name.islower())

another_name = name.upper()
print(another_name)
print(name)

print(name.isupper())
print(another_name.isupper())