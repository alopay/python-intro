# Create a program that prompts the user to enter their age and then determines if they are eligible to vote. If the age is 18 or above, print "You are eligible to vote!" Otherwise, print "You are not eligible to vote yet."

age_input = int(input('Enter your age here: '))

if age_input >= 18 and age_input <= 90:
  print('You are eligible to vote')
elif age_input > 90:
  print("You are too old to vote")
elif age_input < 0:
  print("Invalid Input Option")
else:
  print('You are not eligible to vote yet')
