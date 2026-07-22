#I'm going to write a mini RPG party manager using everything you've learned over the last 11 days.

# Party -------------------------------------------------------------------------------------
party = {
    "Knight": {
        "health": 100,
        "mana": 60,
        "gold": 350,
        "inventory": ["Sword", "Shield", "Potion", "Helmet"]
    },
    "Mage": {
        "health": 50,
        "mana": 150,
        "gold": 120,
        "inventory": ["Staff", "Spellbook"]
    },
    "Archer": {
        "health": 90,
        "mana": 40,
        "gold": 180,
        "inventory": ["Bow", "Arrows", "Dagger"]
    }
}

## Bonus, create function -----------------------------------------------------------------
def display_character(name, stats):
    print(f"{name}")
    for key in stats:
        print(f"  {key}: {stats[key]}")

'''
-- function above replaces this loop --
#use a loop to print character name, health, mana, gold and length of inventory
for character in party:
    health = party[character]["health"]
    mana = party[character]["mana"]
    gold = party[character]["gold"]
    inventory_count = len(party[character]["inventory"])
    print(f"{character} | Health: {health} | Mana: {mana} | Gold: {gold} | Inventory: {inventory_count} items")
'''
for name, stats in party.items():
    display_character(name, stats)


#print the amount of gold in total party -----------------------------------------------------
total_gold = 0
for character in party:
    total_gold += party[character]["gold"]
print(f"Total party gold: {total_gold}")

#find the character with the most hp ----------------------------------------------------------
max_hp = 0
max_character = ""
for character in party:
    if party[character]["health"] > max_hp:
        max_hp = party[character]["health"]
        max_character = character
print(f"{max_character} has the highest health with {max_hp} HP")

#Find who has the largest inventory. ----------------------------------------------------------
largest_inventory = 0
largest_character = ""
for character in party:
    inventory_size = len(party[character]["inventory"])
    if inventory_size > largest_inventory:
        largest_inventory = inventory_size
        largest_character = character
print(f"{largest_character} has the largest inventory with {largest_inventory} items")