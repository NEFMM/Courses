# Conditional expressions = A one-line shortcut for the if-else statement (ternary operator)
#                           print or assign one of two values based on a condition
#                           X if condition else Y

num = 5
a = 6
b = 7
age = 13
temperature = 20
user_role = "guest"

# print("Positive" if num > 0 else "Negative")
# result = "EVEN" if num % 2 == 0 else "ODD"

# print(result)

# max_num = a if a > b else b
# min_num = a if a < b else b

# print(max_num)

# status = "Adult" if age >= 18 else "Child"

# print(status)

# weather = "HOT" if temperature > 20 else "COLD"

# print(weather)

access_level = "Full Access" if user_role == "admin" else "Limited Access"

print(access_level)