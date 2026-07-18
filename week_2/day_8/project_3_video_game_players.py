'''
----- Dictionary representing a video game character --------
GOALS --------------
Print all stats.
Increase the level by 1.
Add a "weapon" key.
Reduce health after taking damage.
Print the updated stats.
---- Bonus challenge ----- without looking up the answer--------------
Add an "inventory" key whose value is a list of items (for example, ["Potion", "Sword", "Shield"]).
Loop through the inventory and print each item.
This combines everything you've learned so far: dictionaries, lists, loops, indexing, and updating data.
------ 1st refactor -----------------------
create a second player
create functions for:
print player stats,
level up
take damage
heal player
add gold
-- BONUS -- for attack scenario -- 

2nd set of function challenges:  --------------------------------------------------------
A revive(player) function that restores a player's health to full.
A buy_item(player, item, cost) function that subtracts gold and adds the item to the inventory.
Prevent purchases if the player doesn't have enough gold.
After each action, call print_player() so you can watch the game state change
'''
# dictionary ----------------------------------------------------
knight = {
    "name": "Knight",
    "health": 100,
    "mana": 75,
    "stamina": 65,
    "level": 3,
    "gold": 1000,
    "inventory": []
}
mage = {
    "name": "Mage",
    "health": 80,
    "mana": 200,
    "stamina": 25,
    "level": 5,
    "gold": 2000,
    "inventory": []
}
dragon = {
    "name": "Dragon",
    "health": 250,
}
# Functions ----------------------------------------------------
def print_player(player):
    for key in player:
        print(f"{key}: {player[key]}")

def level_up(player):
    player["level"] += 1

def take_damage(player, damage):
    player["health"] -= damage

def heal(player, amount):
    player["health"] += amount

def add_gold(player, amount):
    player["gold"] += amount
    print(f"{player['name']} received {amount} gold")

def attack(attacker, defender, damage):
    defender["health"] -= damage
    print(f"{attacker['name']} attacks {defender['name']} for {damage} damage")
    print(f"{defender['name']} has {defender['health']} HP remaining")

def revive(dead_player, healer):
    if dead_player["health"] > 0:
        print(f"{dead_player['name']} is not dead, they have {dead_player["health"]} HP remaining.")
    else:
        dead_player["health"]= 50
        print(f"{healer['name']} uses revive on {dead_player['name']}")
        print(f"{dead_player['name']} has now been revived with {dead_player['health']} HP!")

def buy_item(player, item, cost):
    if player['gold'] < cost:
        print(f"{player['name']} does not have enough gold")
        print(f"{player['name']} purchases {item} for {cost}")
        print(f"{player['name']} has {player['gold']} gold remaining")
    else:
        player["gold"] -= cost
        player["inventory"].append(item)

# starting stats and print --------------------------------------
print("\n----- Starting Knight -----")
print_player(knight)

print("\n----- Starting Mage -----")
print_player(mage)

'''
------increase lvl by 1, add weapon, and reduce HP" -----------------
This was my original solution to the problem, prior to refactor with function.
player["level"] += 1
player["weapon"] = "long sword"
player["health"] -= 10

print("\n----- Player Progress Report-----")
for key in player:
    print(key, player[key])
'''
# --------------- New updated stats and progress report ----------------------
print("\n----- Player Progress Report-----")

add_gold(knight, 5000)
take_damage(knight, 25)
heal(knight, 10)
level_up(knight)
print_player(knight)

## new bonus challenge for attack function ------------------------------------
print("\n-----Battle Scenario-----")
attack(mage, dragon, 50)

## new bonus - revive function -------------------------------------------------
print("\n-----New Bonuses-----")
revive(knight, mage)
buy_item(knight, "sword", 2500)

## Bonus challenge -----------------------------------------------------------
print("\n-----Inventory Updated-----")

knight["inventory"].extend(["shield", "mana potion", "health potion"])
for item in knight["inventory"]:
    print(item)