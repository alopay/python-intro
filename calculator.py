# Write a program that asks the user to enter two numbers and an operator (+, -, *, /). The program should perform the corresponding operation on the numbers and display the result. Make sure to handle division by zero.

print("The symbols needed for this calculator app is as follows: '+ - / *'")
print("""
  + means add
  - means remove
  / means divide
  * means multiply
""")
number1 = int(input("Enter number here: "))
number2 = int(input('Enter the 2nd number here: '))
symbol = input("Enter your symbol here: ")

if symbol == "+":
  total = number1 + number2
  print(f"Answer is {total}")
elif symbol == "-":
  total = number1 - number2
  print(f"Answer is {total}")
elif symbol == '/':
  total = number1 / number2
  print(f"Answer is {total}")
elif symbol == '*':
  total = number1 * number2
  print(f"Answer is {total}")
else:
  print("Invalid Symbol")
