#all players/characters for RPG

knight = {
    "name": "Knight",
    "health": 100,
    "mana": 75,
    "stamina": 65,
    "level": 3,
    "gold": 1000,
    "inventory": ["Sword", "Shield", "Helmet"]
}
mage = {
    "name": "Mage",
    "health": 80,
    "mana": 200,
    "stamina": 25,
    "level": 5,
    "gold": 2000,
    "inventory": ["Staff", "Spellbook", "Mana Potion", "Health Potion"]
}
archer = {
    "name": "Archer",
    "health": 80,
    "mana": 75,
    "stamina": 100,
    "level": 5,
    "gold": 1500,
    "inventory": ["Bow", "Arrows", "Dagger"]
}
party = [
    mage,
    knight,
    archer
]