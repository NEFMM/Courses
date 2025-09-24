# nested loop = A loop within another loop (outer, inner)
#               outer loop:
#                   inner loop:

# outer loop
# for x in range(1, 10):
#     print(x, end="")

# inner loop
# for x in range(3):
#     for x in range(1, 10):
#         print(x, end="")

# combined
# for x in range(3):
#     for y in range(1, 10):
#         print(x, end="")
        
# for x in range(3):
#     for y in range(1, 10):
#         print(y, end="")
#     print()

# challenge: create a grid of symbols
rows = int(input(f"Enter the # of rows: "))
columns = int(input(f"Enter the # of columns: "))
symbol = input(f"Enter a symbol to use: ")

for x in range(rows):
    for y in range(columns):
        print(symbol, end="")
    print()