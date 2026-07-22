print("question 1")
count = 1

while count <= 5:
    print(count)
    count += 1

# Predicted Answer: 1 through 4 will be printed. then close loop?   
    # failed to see the <, which would allow for 5 to be printed.

print("question 2")

while count <= 5:
    print(count)

# Predicted Answer: infinite loop? no escape.. count will always be 1

# Challenge 1 --------------------------
count = 10

while count > 0:
    print(count)
    count -= 2

print("Blast off!")
# line by line write out the outcome:
'''
1. 10
2. 8
3. 6
4. 4
5. 2
7. Blast off!
'''

#Challenge 2 --------------------------
## does this loop end?
x = 5

while x != 0:
    print(x)
    x += 1

    if x == 7:
        break
'''
i believe it is asking if x is not = to ZERO, print what x is (5).
starting at 5, make x + 1, which will never equal zero, thus never end.

later added break to loop.
'''
print("challenge_A")
#Challenge A --------------------------
count = 1

while count <= 5:

    if count == 4:
        break

    print(count)
    count += 1

'''
1
2
3
'''

print("challenge_B")
#Challenge B --------------------------

for number in range(1, 6):

    if number == 3:
        continue

    print(number)
'''
1
2
4
5
'''

print("challenge_Bonus")
#Challenge Bonus --------------------------

count = 1

while count <= 5:

    if count == 3:
        count += 1
        continue

    print(count)
    count += 1

'''
1
2
4
'''
#program got stuck
##REASON - continued loop as python forgets everything before the continue iteration.
##Added count += 1 after if to allow loop to progress after continue.

print("Challenge_Bonus_2")
#Challenge Bonus 2--------------------------

count = 1

while count <= 5:
    count += 1

    if count == 3:
        continue

    print(count)

'''
program would break again? the count function is not in proper order under if statement to continue?
'''