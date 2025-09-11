# Logical operators = evaluate multiple conditions (or, and, not)
#                     or = at least one condition must be True+
#                     and = both conditions must be True
#                     not = inverts the condition (not False, not True)

# temp = 25
# is_raining = False

# if temp > 35 or temp < 0 or is_raining:
#     print(f"The outdoor event it cancelled")
# else:
#     print(f"The outdoor event is still scheduled")

temp = 28
is_sunny = False

if temp >= 28 and is_sunny:
    print(f"It's HOT outside 🥵")
    print(f"It's SUNNY ☀️")
elif temp <= 0 and is_sunny:
    print(f"It's COLD outside 🥶")
    print(f"It's SUNNY ☀️")
elif temp < 28 and temp > 0 and is_sunny:
    print(f"It's WARM outside 😊")
    print(f"It's SUNNY ☀️")
elif temp >= 28 and not is_sunny:
    print(f"It's HOT outside 🥵")
    print(f"It's CLOUDY ☁️")