name = "alopay"

# # Two statement
# if name == "alopay":
#   print('my name is alopay')
# else:
#   print('my name is not alopay')

fruits = ['Watermelon', "Apple", "Banana", "Orange", "Grape"]

print("Guess the fruit in the baskets...")

guess = input("Enter a Fruit name: ")

print(f"Your guessed fruit is {guess.title()}")

if guess.title() in fruits:
  print(f'{guess.title()} is in the basket')
  print("You score 5 points")

else:
  print(f'{guess.title()} is not in the basket')
  print('You lost 5 points')
  