# Tuples and practice
#challenge 1 ----------------------------------------------------------
stats = (100, 75, 60)

health = stats[0]
mana = stats[1]
stamina = stats[2]

print(f"health: {health}\nmana: {mana}\nstamina: {stamina}")
#challenge 2 ----------------------------------------------------------

# OR with unpacking, replace lines 5,6,7 with line 13
health, mana, stamina = stats

print(health)
print(mana)
print(stamina)

#challenge 3 ----------------------------------------------------------
print("challenge #3")
position = (250, 450)
print(f"player is at {position}")

#challenge 4 ----------------------------------------------------------
## Create a set of favorite foods, add one, remove one, print set
print("challenge #4")
favorite_foods={
    "burrito",
    "taco",
    "pizza",
}
favorite_foods.add("sushi")
favorite_foods.remove("taco")
print(favorite_foods)

#challenge 5 ----------------------------------------------------------
##ask the user, "what item are you looking for?"
## if the item exists, print "item found", if not print "item not found."

print("challenge #5")
inventory = {
    "Sword",
    "Shield",
    "Potion"
}

item = input("What item are you looking for? ")

if item in inventory:
    print("Item found!")
else:
    print("Item not found.")