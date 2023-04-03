# Strings

# ord, chr, len, str

# ord()
# Returns an integer value for the given character.
# ord can only convert 1 character
# print(ord("-"))
# print(ord("£"))
# print(ord("E"))
# print(ord("🤗"))

# chr()
# Returns a character value for the given integer.
# chr() handles Unicode characters as well:

# print(chr(69))
# print(chr(129303))
# print(chr(101))
# print("e" in "BELLO")

# len()
# Returns the length of a string.
name = "Alopay UK"
print(len(name))

# str()
# returns a string representation of an object

print("2 * 3")
first = 2
second = 3
first = str(first)

print(first * second)

is_okay = True  # Bool
is_okay = str(is_okay)  # string
print(is_okay)
