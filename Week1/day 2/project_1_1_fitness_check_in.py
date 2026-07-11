# Day 2, Lesson 3
#
# Fitness Calculator
# Author John
# Date: July 11, 2026
#
# Description: This program is for check-ins and will respond to the difference between current weight and goal weight.
# This version of the program is to ONLY calculate IF statments and comparisons with hard coded data. I will add stored info and utilize database next lesson
#
name = "John" 
starting_weight = 202
goal_weight = 190
height = "6'3\""
height_in_inches = 75
print("="*30)
print("        Fitness Check-In")
print("="*30)
print()
print("        User Profile")
print("-"*30)
print(f"name: {name}")
print(f"height: {height}")
print(f"starting weight: {starting_weight} pounds")
print(f"goal weight: {goal_weight} pounds")
print()
print("        Check-In")
print("-"*30)
current_weight = float(input("What is your current weight in pounds? "))
print()
print("        Fitness Report")
print("-"*30)
print(f"Current Weight: {current_weight} pounds")
current_bmi = round((current_weight / (height_in_inches ** 2)) * 703, 1)
if current_weight > starting_weight:
    print(f"{name}, you have gained {str(round(current_weight - starting_weight, 2))} pounds since your starting weight. Let's get back on track!")
elif current_weight > goal_weight:
    print(f"{name}, you have {str(round(current_weight - goal_weight, 2))} pounds to lose to reach your goal weight. Keep up the great work!")
elif current_weight < goal_weight:
    print(f"{name}, Congrats you are below your goal weight by {str(round(goal_weight - current_weight, 2))} pounds! That's awesome!")
else:
    print(f"{name}, you have reached your goal weight! Congratulations!")
print(f"Your current BMI is: {current_bmi}")
print()
if current_bmi < 18.5:
    print("BMI Category: Underweight")
elif current_bmi < 25:
    print("BMI Category: Normal")
elif current_bmi < 30:
    print("BMI Category: Overweight")
else:
    print("BMI Category: Obese")
print("-"*30)
print("BMI (Body Mass Index) is an estimate of body fat based on height and weight. It does not factor in muscle mass, bone density, overall body composition.")
print("-"*30)
print()
print("Thank you for using the Fitness Check-In Program!")