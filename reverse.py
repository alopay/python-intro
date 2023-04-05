name = "AbdulHakeem"

# String Slicing Inversion or Reverse
# print("This is normal String Slicing and it's a 2 step slicing")
# print(name[::2])

# print("This is inverted String Slicing")
# print(name[::-1]) # -1 on the column to invert the values

# print("This is an inverted String Slicing with 2 step slicing")
# print(name[::-2]) # -2 

fruits = "WaterMelon"

print(fruits[3]) # Indexing

vegetable = "Onion"

# test = vegetable[-2:]
# print(test)

# var1 = '' # Water
# var2 = "" # Melon
test = fruits[:5] # Slicing
print(test)

inverted_test = test[::-1] # Reverse Slice
print(inverted_test)

inverted_test1 = test[::-2]
print(inverted_test1)

"""
  In string slicing,
  first column : deals with the order of slicing from:to
  second column : deals with the step
  nb: if the second column step is in negative format -1, -2; it steps from behind
"""