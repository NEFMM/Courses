# Python compound interest calculator

FinalAmount = 0
Principle = 0
Rate = 0
Time = 0

while Principle <= 0:
    Principle = float(input(f"Enter the principal amount: "))
    if Principle <= 0:
        print(f"Principle can't be less than or equal to zero")
    else:
        break
        
while Rate <= 0:
    Rate = float(input(f"Enter the Interest Rate: "))
    if Rate <= 0:
        print(f"Interest can't be less than or equal to zero")
    else:
        break
        
while Time <= 0:
    Time = int(input(f"Enter the time in years: "))
    if Time <= 0:
        print(f"Time can't be less than or equal to zero")
    else:
        break
        
FinalAmount = Principle * (pow(1 + (Rate / 100), Time))
print(f"Balance after {Time} years is: ${FinalAmount:.2f}")