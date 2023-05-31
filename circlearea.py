print("""
  The aim of this code is to calculate the areas of rectangles, squares and circle
""")

# inputs are always str

# formular for circle = 3.14 * r * r or 3.14 * r **2 

radius = int(input('Enter the radius of the circle: '))


area = 3.14 * radius**2

print(
  f'The area of a circle of radius {radius} is {area}.'
)

