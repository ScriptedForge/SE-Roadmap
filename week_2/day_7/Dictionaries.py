## practice -----------------------
car = {
    "make": "Subaru",
    "model": "STI",
    "year": 2020,
    "color": "white"
}

#print(car["make"])
#print(car["model"])
#print(car["year"])
#print(car["color"])

## Mini Challenge -------------------
#print("mini challenge")

car = {
    "make": "Subaru",
    "model": "STI"
}

car["year"] = 2020
car["make"] = "Honda"

#print(car)

## Bonus Challenge ----------------------
#print("bonus challenge")
me = {
    "name": "John",
    "age": 30,
    "favorite language": "C++",
    "favorite car": "porsche 911",
    "height": "6'3"
}
#print(me["name"])
me["career"] = "Software Engineer"
me["favorite language"]= "Python"
#print(me)

## Final Challenge ----------------------
print("Final challenge")

print("Welcome!")

favorites = {}

favorites["color"]=input("Enter your favorite color:")
favorites["animal"]=input("Enter your favorite animal:")
favorites["food"]=input("Enter your favorite food:")

print("\nYour Favorites:")
print("favorite animal:", (favorites["animal"]))
print("favorite color:", (favorites["color"]))
print("favorite food:", (favorites["food"]))

change = input("\nwould you like to change one? (yes/no)")

'''
this version below is better, but not GREAT. it SHOULD be a loop to circle back and give user a second chance to correct the spelling mistake.
    update - created while loop to solve afformentioned problem, also added strip and lower to allow case sensitive errors.
'''

if change == "yes":
    which_one = input("which one?").lower().strip()
    while which_one not in favorites:
        print("entry does not match, try again")
        which_one = input("which one?")

    favorites[which_one] = input("enter the new value: ")
    print("updated Favorites:")
    print("favorite animal:", favorites["animal"])
    print("favorite color:", favorites["color"])
    print("favorite food:", favorites["food"])

print("\nThank you for your entries.")

'''
THIS was my first iteration, which is redundant.. above is the 2nd attempt at a more all inclusive line to condense the code"
    if which_one == "animal":
     favorites["animal"] = input("enter your new favorite animal:")
    elif which_one == "color":
     favorites["color"] = input("enter your new favorite color:")
    elif which_one =="food":
     favorites["food"] = input("enter your new favorite food:")
'''
