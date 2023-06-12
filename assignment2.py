# Challenge 3: Grade Classifier
# Write a program that asks the user to enter a numeric grade and outputs the corresponding letter grade based on the following scale:

# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: 0-59

grade = int(input('Enter your score here: '))

if grade >= 90 and grade <= 100:
  print(f"Your score is {grade}")
  print("Congratulations! You got an A")
elif grade <= 89 and grade >= 80:
  print(f"Your score is {grade}")
  print("Congratulations! You got an B")
elif grade <= 79 and grade >= 70:
  print(f"Your score is {grade}")
  print('Congratulations! You got a C')
elif grade >= 60 and grade <= 69:
  print(f"Your score is {grade}")
  print('Congratulations! You got a D')
elif grade >= 0 and grade <= 59:
  print(f'Your score is {grade}')
  print("Oops! you got an F")
else:
  print("Invalid Format!!!")