# while loop = execute some code WHILE some conditions remains true

# name = input(f"Enter your name: ")

# while name == "":
#     print(f"You did not enter your name")
#     name = input(f"Enter your name: ")

# print(f"Hello {name}")

# ----

# age = int(input(f"Enter your age: "))

# while age < 0:
#     print(f"Age can't be negative")
#     age = int(input(f"Enter your age: "))
    
# print(f"You are {age} years old")

# ----

# food = input(f"Enter a food you like (q to quit): ")

# while not food == "q":
#     print(f"You like {food}")
#     food = input(f"Enter a food you like (q to quit): ")

# print(f"Bye!")

# ----

num = int(input("Enter a # between 1 - 10: "))

while num < 1 or num > 10:
    print(f"{num} is not valid")
    num = int(input("Enter a # between 1 - 10: "))
    
print(f"Your number is {num}")