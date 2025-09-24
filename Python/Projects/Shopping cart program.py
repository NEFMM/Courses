# Shooping cart program

foods = []
prices = []
total = 0

while True:
    food = input(f"Enter a food you want to buy (q to quit): ")
    if food.lower() == 'q':
        break
    else:
        foods.append(food)
        
        price = float(input(f"Enter the price of a {food}: $"))
        prices.append(price)
        
print(f"----- YOUR CART -----")

for food in foods:
    print(food, end=" ")

for price in prices:
    total += price
    
print(f"\nYour total is: ${total:.2f}")