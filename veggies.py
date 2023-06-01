name = "alopay"

# # Two statement
# if name == "alopay":
#   print('my name is alopay')
# else:
#   print('my name is not alopay')

popular_veggies = "Tomato"

print("Guess the most popular Vegetable")

guess = input("What is the most popular Vegetable? ")

print(f"Your guessed veggies is {guess.title()}")


if guess.title() == popular_veggies:
  print('You guessed right')
  print(f"The vegetable is {popular_veggies}")

else:
  print('You guessed wrong')
  print(f"The vegetable is {popular_veggies}")
  