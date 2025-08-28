# Create a program that declares and fills a 2x2 multidimensional matrix with 
# random integers and then prints the sum of the  elements of all the elements of the matrix

import random

num_lines = 2
num_columns = 2
sum = 0

matrix = []

for i in range(num_lines):
    line = []
    for j in range(num_columns):
        r_number = random.randint(0, 5)
        line.append(r_number)
    matrix.append(line)

print(f"Matrix 2x2: ")

for line in matrix:
    print(line)

for line in matrix:
    for n in line:
        sum += n

print(f"Sum of all elements: {sum}")