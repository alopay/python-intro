# conditional statement

# if, elif and else keywords

age = int(input("Enter Your age here: "))

if age < 18: # age < 18 is an expression
  print("Oops! You are not qualified")
else:
  print("Congratulations! You are qualified...")

jamb_score = int(input("Enter Your recent Jamb Score here: "))

if jamb_score < 200:
  print("You are qualified for Polytechnic")
else:
  print("You are qualified for a University")