# Python Calculator

operator = input(f"Enter an operator: ")

num0 = float(input(f"Enter first number: "))
num01 = float(input(f"Enter second number: "))

num2 = 0
if operator == "+":
    num2 = num0 + num01
    print(f"The result is {round(num2, 3)}")
elif operator == "-":
    num2 = num0 - num01
    print(f"The result is {round(num2, 3)}")
elif operator == "*":
    num2 = num0 * num01
    print(f"The result is {round(num2, 3)}")
elif operator == "/":
    num2 = num0 / num01
    print(f"The result is {round(num2, 3)}")
else:
    print(f"{operator} is not a valid operator.")