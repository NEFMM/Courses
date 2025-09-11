# validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input(f"Enter your username: ")

if len(username) > 12:
    print(f"Your username can't be more than 12 characters")
elif not username.find(" ") == -1:
    print(f"Your username can't contain spaces")
elif not username.isalpha():
    print(f"Your username can't contain digits")
else:
    print(f"Welcome {username}")
    