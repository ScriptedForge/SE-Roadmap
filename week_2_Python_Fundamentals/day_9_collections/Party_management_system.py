'''
-----Today is practicing collections and iterations ------
==Goals==
Display all characters
Heal every character
Damage one character
Find a character by name
Award gold
Level up characters
Print party statistics
'''

## Characters ----------------------------------------------------
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
archer = {
    "name": "Archer",
    "health": 80,
    "mana": 75,
    "stamina": 100,
    "level": 5,
    "gold": 1500,
    "inventory": []
}
party = [
    mage,
    knight,
    archer
]

## Functions --------------------------------------------------
def level_up(character):
    character["level"] += 1

def display_party_details(party):
    print("="*10+ "PARTY"+ "="*10)
    for character in party:
        print("-"*25)
        for key in character:
            print(f"{key}: {character[key]}")
    print("="*25)

def heal_party(party, amount):
    for character in party:
        character["health"] += amount
        if character["health"] > 1000:
            character["health"] = 1000
        print(f"{character["name"]} has been healed for {amount} HP")

def heal_character(party, name, amount):
    for character in party:
        if character["name"].lower() == name.lower():
            character["health"] += amount
            if character["health"] > 1000:
                character["health"] = 1000
            print(f"{character['name']} has been healed for {amount} HP")
            return
    print(f"No character named {name} found.")

def damage_character(party, name, amount):
    for character in party:
        if character["name"].lower() == name.lower():
            character["health"] -= amount
            if character["health"] <= 0:
                character["health"] = 0
                print(f"{character['name']} has been damaged for {amount} HP")
                print(f"{character['name']} has fallen")
            else:
                print(f"{character['name']} has been damaged for {amount} HP")
                print(f"{character['name']} has {character['health']} HP remaining")
            return
    print(f"No character named {name} found.")


'''
# finding character function
def find_character(party, name):
    for character in party:
        if character["name"].lower() == name.lower():
            return character
    return None

character = find_character(party, "Mage")
if character is None:
    print("Character not found.")
else:
    character["health"] += amount
'''


## damage Character ------------------------------------------
damage_character(party, "knight", 150)

## Heal Characters ------------------------------------------
heal_party(party, 20)
heal_character(party, "Mage", 30)

## Display Characters ------------------------------------------
display_party_details(party)
heal_character(party, "Mage", 30)

print("="*12+ " PARTY "+ "="*12)
for character in party:
    print(f"{character['name']} | HP: {character['health']} | Gold: {character['gold']} ")
print("="*31)

## Level up Characters -----------------------------------------
for character in party:
    level_up(character)
    print(f"{character['name']} is now level {character['level']}")