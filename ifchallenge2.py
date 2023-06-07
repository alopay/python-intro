# Write a program that checks if a number is even or odd. If the number is even, print "Even number." Otherwise, print "Odd number."

user_input = int(input('Enter a number here: '))
print(f"number is {user_input}.")


if user_input % 2 == 0: # 13 / 2 remainder == 1 and 1 == 0
  print("Even number")
else:
  print("Odd number")