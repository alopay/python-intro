# Create a program that calculates the total price of a product based on its quantity and unit price. Ask the user to enter the quantity and unit price, then apply a discount of 10% if the quantity is greater than 10. Print the total price after considering the discount.



quantity = int(input("Enter the quantity of the product: "))
unit_price = int(input("Enter the unit price of the product: "))
total = quantity * unit_price

if quantity >= 20:
  new_total = total * 0.8
  print(f"Your initial value is {total} naira")
  print("You got 20% discount!")
  print(f"Your new total value is {new_total} naira")
elif quantity > 10:
  new_total = total * 0.9
  print(f"Your initial value is {total} naira")
  print("You got 10% discount!")
  print(f"Your new total value is {new_total} naira")
elif quantity > 5:
  new_total = total * 0.95
  print(f"Your initial value is {total} naira")
  print("You got 5% discount!")
  print(f"Your new total value is {new_total} naira")
else:
  print(f"The total value of the product is {total} naira")
