# Exercise 2 Simple Shopping Cart

item = input("What item would you like to buy? ")
price = float(input("What is the price of the item? "))
quantity = int(input("How many of this item would you like to buy? "))

total = price * quantity

print(f"You have bought {quantity} {item}(s)")
print(f"Your total is: ${total}")