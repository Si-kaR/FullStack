rivers = [
{"name": "Nile", "length": 4157},
{"name": "Yangtze", "length": 3434},
{"name": "Murray-Darling", "length": 2310},
{"name": "Volga", "length": 2290},
{"name": "Mississippi", "length": 2540},
{"name": "Amazon", "length": 3915}
]


# Task 1 - In a In a for loop, print out each river's name!
print("\nTask 1 - In a In a for loop, print out each river's name!")
for river in rivers:
    print(river["name"])

# Task 2 - In another for loop, add up and print out the total length of all the rivers!
print("\nTask 2 - In another for loop, add up and print out the total length of all the rivers!")
total_length = 0
for river in rivers:
    total_length += river["length"]

print("Total length of all rivers:", total_length,"\n")



#Extensions
# 1. Print out every river's name that begins with the letter M !
print("\n#Extensions\n#1. Print out every river's name that begins with the letter M !")
for river in rivers:
    if river["name"].startswith("M"):
        print(river["name"])

# 2. The length of the rivers are in miles. Print out every river's length in kilometres! (1 mile is
# roughly 1.6 km)
print("\n# 2. The length of the rivers are in miles. Print out every river's length in kilometres!\n#Hint: (1 mile is roughly 1.6 km)")
for river in rivers:
    length_km = river["length"] * 1.6
    print(f"{river['name']} - Length: {length_km:.2f} km")