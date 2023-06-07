# Write a program that asks the user to enter two numbers and checks if the first number is divisible by the second number. If it is divisible, print "The first number is divisible by the second number." Otherwise, print "The first number is not divisible by the second number."

user_input1 = int(input("Enter the First number: "))
user_input2 = int(input('Enter the second number: '))

if user_input1 % user_input2 == 0:
  print("The first number is divisible by the second number.")
else:
  print("The first number is not divisible by the second number.")