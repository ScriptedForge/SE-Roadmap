#displaying party or player/character details

def display_party_details(party):
    print("="*10+ "PARTY"+ "="*10)
    for character in party:
        print("-"*25)
        for key in character:
            print(f"{key}: {character[key]}")
    print("="*25)


## which one is better display?
def display_character(name, stats):
    print(f"{name}")
    for key in stats:
        print(f"  {key}: {stats[key]}")

def print_player(player):
    for key in player:
        print(f"{key}: {player[key]}")
