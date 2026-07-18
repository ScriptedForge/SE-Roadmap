print("question 1:")
numbers = [10, 20, 30]

print(numbers[1])
# break ----------------------------------------
print("question 2:")
animals = ["dog", "cat"]

animals.append("bird")

print(animals)
# break ----------------------------------------
print("question 3:")
for i in range(4):
    print(i)
# break ----------------------------------------
print("question 4:")
score = 82

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")
# break ----------------------------------------
print("question 5:")
secret = 7

guess = 5

while guess != secret:
    guess += 1

print(guess)

# break ----------------------------------------
print("Challenge 1")
car = {
    "brand": "Subaru",
    "model": "STI",
    "year": 2020
}

print(car["model"])
# break ----------------------------------------
print("challenge 2")
car["year"] = 2021

print(car["year"])
# break ----------------------------------------
print("challenge 3")
car["color"] = "Blue"

print(car)

