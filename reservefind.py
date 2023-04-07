# Swap case

sentence = "Hello, I am Bello AbdulHakeem"

# print(sentence)
# print(sentence.swapcase())

# startswith()

# print(sentence.startswith('llo', 0, 20))
# print(sentence.startswith('llo', 2, 20))

# endswith
# print(sentence.endswith("lo", 0, 17))

# print(sentence.endswith("am", 0, 11))
# print(sentence.startswith('am', 9))

# find() is used to find the lowest index position of a targetted substring in the string
print(sentence.find("wt"))
print(sentence.find("Ab"))

# if the output of our find method is -1, substring is not in the targetted string

print(sentence.index("tx"))

# find and index does the same function but, 'index' raises an error if position not found whereas 'find' doesn't
