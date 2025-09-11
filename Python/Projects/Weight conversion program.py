# Python weight converter

weight = float(input(f"Enter your weight: "))
unit = input(f"Kilograms or Pounds? (K or L): ")

if unit == "K" or "k":
    weight = weight * 2.205
    unit = "Lbs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
elif unit == "L" or "l":
    weight = weight / 2.205
    unit = "Kgs."
    print(f"Your weight is: {round(weight, 1)} {unit}")
else:
    print(f"{unit} was not valid")