print("""
We will be taking info of university students
""")

first_name = input("Enter Your First Name: ")
last_name = input("Enter Your Last Name: ")
other_name = input("Enter Your Other Name: ")
year_of_birth = int(input("Enter Your BirthYear. e.g 1990: "))
# department = input("Enter Your preferred Department")

age = 2023 - year_of_birth

print(
  f"""
  Dear {first_name.title()} {last_name.title()}, Your info has been stored 
  and the {other_name.title()} has been included.
  """)

print(f"You are {age} years old")