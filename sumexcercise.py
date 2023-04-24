# Python lexical structure

print("Hello Wolrd")


x = [1, 2, 3]
print(x[1:2])


fruits = ['banana', 'pawpaw', 'apple']

print(fruits[2][:4])

text = 'foobar'[2:5]

print(text)

print(f'The output of the following is {fruits[-2][:3].upper()}')

print("Tade",
      "Tolu",
      "Fola"
     )

print(text.title())


items_needed = {
  'fruits': ["Apples", "Orange"],
  'vegetables': ("Onion", 'Tomato'),
  'cereal': "Golden Morn",
  'Total_amount': 400.32
}

print(items_needed)
print(items_needed['cereal'])

fruits = items_needed['fruits']
print(fruits)
print(fruits[0])


x = 1; y = 2; z = 3
print(x, y, z)

x, y, z = 1, 4, 5
print(x, y, z)

name = "tade" # This is a side comment

print(name)

new_name = "Tolu # This is another comment"

print(new_name)