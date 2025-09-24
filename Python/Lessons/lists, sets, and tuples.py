# collection = single "variable" used to store multiple values
#   List = [] ordered and changeable. Duplicates OK
#   Set = {} unordered and immutable, but Add/Remove OK. NO duplicates
#   Tuple = () ordered and unchangeable. Duplicates OK. FASTER

# fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "coconut"]

# fruits[2] = "pineapple" 
# fruits.append("pineapple")
# fruits.remove("apple")
# fruits.insert(0, "pineapple") 
# fruits.sort()
# fruits.reverse()
# fruits.clear()
# print(fruits.index("cherry"))
# fruits.count("banana")

# fruits = {"apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "coconut"}

# fruits.add("pineapple")
# fruits.remove("banana")
# fruits.pop()

fruits = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango", "coconut")

# fruits.index("cherry")
# print(fruits.index("cherry"))
# print(fruits.count("banana"))


# print(dir(fruits))
# print(help(fruits))
# print(len(fruits))
# print("pineapple" in fruits)

# print(fruits)
# print(fruits[1])
# print(fruits[0:2])
# print(fruits[::2])

for fruits in fruits:
    print(fruits)