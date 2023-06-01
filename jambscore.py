# conditional statement

# if, elif and else keywords

jamb_score = int(input("Enter Your recent Jamb Score here: "))

if jamb_score < 150:
  print(f"Your Jamb Score is {jamb_score}")
  print("You are qualified for College of Education")
elif jamb_score >= 150 and jamb_score < 180: # from 150 to 179
  print(f"Your Jamb Score is {jamb_score}")
  print("You are qualified for a Polytechnic")
elif jamb_score >= 180 and jamb_score < 200:
  print(f"Your Jamb Score is {jamb_score}")
  print("You are qualified for a State University")
elif jamb_score >= 200 and jamb_score < 401:
  print(f"Your Jamb Score is {jamb_score}")
  print("You are qualified for a Federal University")
else:
  print(f"Your Jamb Score is {jamb_score}")
  print("Invalid Jamb Score")