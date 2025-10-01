# dictionary = a collection of {key:value} pairs
#              ordered and changeable. No duplicates

# create a dictionary
capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

# print(dir(capitals))
# print(help(capitals))
# print(capitals.get("USA"))
# print(capitals.get("Japan"))

# check if a key exists
# if capitals.get("Japan"):
#     print("That capital exists")
# else:
#     print("That capital doesn't exist")    

# capitals.update({"Germany": "Berlin"})
# capitals.update({"USA": "Detrot"})
# capitals.pop("China")
# capitals.popitem()
# capitals.clear()

# print(capitals)

# --------------------------------------------------

# print only the keys in the dictionary
# keys = capitals.keys()
# # print(keys)

# print only the values in the dictionary
# for key in capitals.keys():
    # print(key)
    
# --------------------------------------------------

# print only the values in the dictionary
# values = capitals.values()
# # print(values)

# for value in capitals.values():
    # print(value)
    
# items = capitals.items()
# # print(items)

# for key, value in capitals.items():
#     print(f"{key} : {value}")