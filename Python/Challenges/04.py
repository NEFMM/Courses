# Write a program in Java/Python that receives a list of city names and returns a HashMap 
# where the keys are the character numbers of the city names and the values are string 
# lists containing all the city names with that number of characters.

city = ["Tokyo", "New York", "Los Angeles", "Chicago", "Houston", "Phoenix", "Philadelphia", "San Antonio", "San Diego", "Dallas"]

hashmap = {}

for i in range(len(city)):
    x = city[i]

    count = 0
    for j in x:
        count = count + 1

    if count not in hashmap:
        hashmap[count] = []

    hashmap[count] += [x]

print(hashmap)