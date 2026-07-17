'''
This is going to be a program to input items needed for a grocery list.
    user prompts to continue entering more items, y/n
        print list after editing
    at any point, user can add another item?
requirements:
    use one Loop
    one list
    user input
'''
## List --------------------------------------------------------
grocery_list = []

## brief welcome ------------------------------------------------
print("="*50)
print("Welcome to Grocery List Manager!")

## adding items ------------------------------------------------
print('\nTo finish your list at any point, type "done"')
print()
while True:
    user_input = input("add item: ")
    if user_input == "done":
        break
    grocery_list.append(user_input)

## final print ------------------------------------------------
print()
print("Your Grocery List:")
for item in grocery_list:
    print(item)