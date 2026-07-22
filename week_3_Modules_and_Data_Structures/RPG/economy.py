# Add, check gold, sell item, purchase item

def add_gold(player, amount):
    player["gold"] += amount
    print(f"{player['name']} received {amount} gold")

def buy_item(player, item, cost):
    if player['gold'] < cost:
        print(f"{player['name']} does not have enough gold")

    else:
        player["gold"] -= cost
        player["inventory"].append(item)
        print(f"{player['name']} purchases {item} for {cost}")
        print(f"{player['name']} has {player['gold']} gold remaining")
