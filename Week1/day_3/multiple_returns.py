print("challenge_1")
def rectangle(length, width):
    area = length * width
    perimeter = (length * 2) + (width * 2)

    return area, perimeter


area, perimeter = rectangle(10, 5)

#area should print as 50
#perimeter should print as 30
#instead of printing both answers once, right away within the function, i can print either or pull either or as needed in later data analysis

print(area)
print(perimeter)

print("challenge_2")
def rectangle(length, width):
    area = length * width
    perimeter = (length * 2) + (width * 2)

    return perimeter, area

#this is a test to see if two identical functions can exist without replacing the other... This should be the replacement
#i notice the return "area, perimeter" have been swapped. i dont believe this will affect the product"

print(area)
print(perimeter)

print("challenge_3")
def rectangle(length, width):
    area = length * width
    perimeter = (length * 2) + (width * 2)

    return area, perimeter

answer = rectangle(10, 5)

print(answer)

# Because rectangle is established in the function, it will not display as the "answer = rectangle(10, 5)"
#prediction: im asking it to print answer, which is redefined by the function. which may give the same answer of area and perimeter separately?