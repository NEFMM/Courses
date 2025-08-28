# import math

# radius = float(input(f'Enter the radius of a circle: '))

# circumference = 2 * math.pi * radius

# print(f"The circumference is: {round(circumference, 2)}cm")

# ---

# import math

# radius = float(input("Enter the radius of a circle: "))

# area = math.pi * pow(radius, 2)

# print(f"The area of the circle is: {round(area, 2)}cm²")

# ---

import math

a = float(input(f"Enter side A: "))
b = float(input(f"Enter side B: "))

c = math.sqrt(pow(a, 2) + pow(b,2))

print(f"Side C = {round(c, 2)}")