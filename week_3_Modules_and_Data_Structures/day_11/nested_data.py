'''
Dictionaries PART 2, Nested data
including multiple dictionaries within another. like folders.

'''

#challenge 1 -------------------------------------------------------
'''
Print the Mage's mana.
Add 50 gold to the Knight.
Subtract 30 health from the Mage.
Print both updated dictionaries.
'''

party = {
    "Knight": {
        "health": 100,
        "mana": 60,
        "gold": 300,
        "inventory": [
            "Sword",
            "Shield",
            "Potion"
        ]
    },

    "Mage": {
        "health": 80,
        "mana": 150,
        "gold": 120,
        "inventory": [
            "Staff",
            "Spellbook",
            "Potion"
        ]
    }
}

print(party["Mage"]["mana"])
party["Knight"]["gold"]+=50
party["Mage"]["health"]-= 30
print(party["Knight"])
print(party["Mage"])

#challenge 1 -------------------------------------------------------
print("challenge 2")
'''
Print the Knight's second inventory item.
Print the Mage's last inventory item.
Add "Helmet" to the Knight's inventory.
Remove "Potion" from the Mage's inventory.
Print both inventories.
'''

print(party["Knight"]["inventory"][1])
print(party["Mage"]["inventory"][-1])
party["Knight"]["inventory"].append("Helmet")
party["Mage"]["inventory"].remove("Potion")
print(party["Knight"]["inventory"])
print(party["Mage"]["inventory"])

#mini challenge -----------------------------------------------------
'''
print this:
Knight has 4 items.
Mage has 2 items.
'''

knight_count = len(party["Knight"]["inventory"])
mage_count = len(party["Mage"]["inventory"])
print(f"Knight has {knight_count} items.")
print(f"Mage has {mage_count} items.")

print("\nchallenge 3")
for character in party.values():
    for key in character:
            print(f"{key}: {character[key]}")
    