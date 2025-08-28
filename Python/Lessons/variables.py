# Variable = A container for a value (string, integer, float, boolean)
#            A variable behaves if it was the value it contains


# Strings
first_name = "Enzo"
food = "pizza"
email = "Enzo123@fake.com"

print(first_name)
print(f"Hello {first_name}!")
print(f"You like {food}")
print(f"Your email is: {email}")


# Integers
age = 25
quantity = 3
num_of_students = 30

print(f"You are {age} years old")
print(f"You are buying {quantity} items")
print(f"Your class has {num_of_students} students")


# Float
price = 10.99
gpa = 3.2
distance = 5.5

print(f"The price is R${price}")
print(f"You gpa is: {gpa}")
print(f"You ran {distance}km today")


# Boolean
is_student = False
for_sale = True

print(f"You are a student: {is_student}")

if is_student:
    print(f"You are a student")
else:
    print(f"You are NOT a student")

if for_sale:
    print(f"This item is for sale")
else:
    print(f"This item is NOT avaiable")