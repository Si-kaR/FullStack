animals = [
{"name": "capybara", "group": "mammal", "weight": 110},
{"name": "hedgehog", "group": "mammal", "weight": 0.5},
{"name": "bearded dragon", "group": "reptile", "weight": 1},
{"name": "tortoise", "group": "reptile", "weight": 40},
{"name": "hummingbird", "group": "bird", "weight": 0.01},
{"name": "elephant", "group": "mammal", "weight": 10000},
{"name": "ostrich", "group": "bird", "weight": 280},
{"name": "python", "group": "reptile", "weight": 180},
{"name": "blue whale", "group": "mammal", "weight": 300000},
{"name": "lion", "group": "mammal", "weight": 350}
]

# Let's consider the following tasks:
# 1. Print out all the animals names that are heavier than 100 pounds!
# 2. Print out the heaviest animal!
# 3. Print out the lightest animal!
# 4. Print out all mammals as a list!


# # 1. Print out all the animals names that are heavier than 100 pounds!
    #  Loop through the dataset and 
    #  Check their weights
    #  display weights greater than the 100

for animal in animals:
    if animal["weight"] > 100:
        print (animal["name"])

# # 2. Print out the heaviest animal!
    # Loop through the dataset 
    # Check and compare their weight
    # display the largest (heaviest) weight 
heaviest_animal = animal[0]

for animal in animals:
    if animal["weight"] > heaviest_animal["weight"]:
        heaviest_animal = animal

print(heaviest_animal)

