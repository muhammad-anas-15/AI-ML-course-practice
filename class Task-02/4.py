import random

# Categories
mains = ["chapli kabab", "namkeen gosht", "karahi",
         "shinwari tikka", "peshawari pulao"]

sides = ["raita", "salad", "naan", "chutney"]

drinks = ["doodh patti", "green tea", "lassi", "sugarcane juice"]

desserts = ["firni", "jalebi", "kheer", "gulab jamun"]


# Function to generate random price
def get_price(category):
    if category == "main":
        return random.randint(300, 800)
    elif category == "side":
        return random.randint(50, 200)
    elif category == "drink":
        return random.randint(50, 150)
    elif category == "dessert":
        return random.randint(100, 250)


# (a) Random Combo Meal
print("===== RANDOM COMBO MEAL =====")

combo = {
    "Main": random.choice(mains),
    "Side": random.choice(sides),
    "Drink": random.choice(drinks),
    "Dessert": random.choice(desserts)
}

combo_total = 0

for category, item in combo.items():
    if category == "Main":
        price = get_price("main")
    elif category == "Side":
        price = get_price("side")
    elif category == "Drink":
        price = get_price("drink")
    else:
        price = get_price("dessert")

    combo_total += price
    print(f"{category}: {item} - Rs. {price}")

print("Total: Rs.", combo_total)


# (b) Party Platter (No repeats)
print("\n===== PARTY PLATTER =====")

party_mains = random.sample(mains, 3)
party_sides = random.sample(sides, 2)
party_drinks = random.sample(drinks, 2)
party_dessert = random.sample(desserts, 1)

party_total = 0

print("\nMains:")
for item in party_mains:
    price = get_price("main")
    party_total += price
    print(f"{item} - Rs. {price}")

print("\nSides:")
for item in party_sides:
    price = get_price("side")
    party_total += price
    print(f"{item} - Rs. {price}")

print("\nDrinks:")
for item in party_drinks:
    price = get_price("drink")
    party_total += price
    print(f"{item} - Rs. {price}")

print("\nDessert:")
for item in party_dessert:
    price = get_price("dessert")
    party_total += price
    print(f"{item} - Rs. {price}")

print("\nParty Platter Total: Rs.", party_total)