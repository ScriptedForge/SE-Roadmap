# Day 2, Lesson 2
#
# Fitness Calculator
# Author John
# Date: July 11, 2026
#
# Description: This program will calculate your BMI and how many weeks it will take to reach your goal weight.
#
# Get User Input
name = input("What is your name? ")
height = input("What is your height? (ie, 6'3\"): ")
parts = height.split("'")
height_in_inches = int(parts[0]) * 12 + int(parts[1].rstrip('"'))
weight = float(input("What is your weight in pounds? "))
goal_Weight = float(input("What is your goal weight in pounds? "))
# Start Display
print("="*30)
print("        Fitness Report")
print("="*30)
print()
print(f"Name: {name}")
print(f"Height: {height}")
print(f"Weight: {weight} pounds")
# Perform Calculations
print(f"BMI: {round((weight / (height_in_inches ** 2)) * 703, 1)}")
print("-"*30)
print(f"Goal Weight: {goal_Weight} pounds")
print(f"Weight to Lose: {round(weight - goal_Weight, 2)} pounds")
print(f"Goal BMI: {round((goal_Weight / (height_in_inches ** 2)) * 703, 1)}")
print(f"Weeks to Lose Weight: {round((weight - goal_Weight) / 1.5, 2)} weeks")
print("-"*30)
print("Thank you for using the Fitness Calculator!")