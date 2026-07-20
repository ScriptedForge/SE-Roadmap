#Bonus challenge ----------------------------------------------------------
'''Create a tiny RPG inventory manager.
Requirements:
Character stats stored in a tuple
Inventory stored in a set
At least three functions
Use an if statement
Use a loop
Allow the user to search for an item
Print the final inventory
'''
import random
# functions ----------------------------------------------------------------
def defeat_goblin():
    boss_loot = {"gold", "artifact", "sword", "potion"}
    found_item = random.choice(tuple(boss_loot))
    your_inventory.add(found_item)
    print("You have slain the goblin")
    print(f"You found {found_item}")

def drop_item(item):
    if item in your_inventory:
        your_inventory.remove(item)
        print(f"{item} dropped")
    else:
        print("You don't have that item.")
        
def choose_path(direction):
    if direction == "left":
        return "goblin avoided"
    elif direction == "right":
        return "you have encountered a goblin"
    else:
        return "invalid path"
# Stats stored in tuple ----------------------------------------------------
stats = (100, 75, 60)
health, mana, stamina = stats

# Inventory stored in set --------------------------------------------------
your_inventory = {
    "staff",
    "health portion",
    "mana portion",
}
# Introduction -------------------------------------------------------------
name = input("enter your name: ")
print(f"Hello, {name}")
print("While traveling down a road to a forest, you notice the path splits.. you have two choices.")

# utilize funcitons --------------------------------------------------------
path = input("Choose a path (left/right): ").strip().lower()
print(choose_path(path))
if path == "right":
    choice = input("would you like to fight? (y/n) ").strip().lower()
    if choice == "y":
        defeat_goblin()
    else:
        print("You carefully sneak away.")
# Search for an item --------------------------------------------------------
print("you're begining to feel hungry.. you notice a food cart but wonder if you have the gold to buy anything.")
item = input("\nWhat item are you looking for? ").strip().lower()

# If statement --------------------------------------------------------------
if item in your_inventory:
    print("Item found!")
else:
    print("Item not found.")

## print final inventory, (using loop) --------------------------------------
print("\nInventory Report:")
for item in your_inventory:
    print(item)

drop = input("Would you like to drop an item? (y/n): ").lower()

if drop == "y":
    item = input("Which item? ").lower()
    drop_item(item)