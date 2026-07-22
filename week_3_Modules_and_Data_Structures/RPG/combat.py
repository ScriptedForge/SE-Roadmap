## Combat and functions for RPG

def level_up(character):
    character["level"] += 1

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

#PVP
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
