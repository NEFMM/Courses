# Write a program that initializes a literal array of strings with the names 
# of the months of the year and then print only the months with more than 5 letters

Y_Months = ["January", "February", "March", "April", "May", "June",
            "July", "August", "September", "October", "November", "December"]

print(f"Months with more than 5 letters: ")

for month in Y_Months:
    if len(month) > 5:
        print(month)