# Python temperature conversion program

unit = input(f"Is this temperature in Celsius or Fahrenheit (C/F)? ")
temp = float(input(f"Enter the temperature: "))

if unit == 'C':
    temp = round((temp * (9/5)) + 32, 1)
    print(f"The temperature in Fahrenheit is: {temp}ºF")
elif unit == 'F':
    temp = round((temp - 32) * (5/9), 1)
    print(f"The temperature in Celsius is: {temp}ºC")
else:
    print(f"{unit} is an invalid unit of measurement")