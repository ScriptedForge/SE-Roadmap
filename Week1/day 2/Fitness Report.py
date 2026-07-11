#Day 2, Lesson 2
#Fitness Calculator
#Author John
#Date: July 11, 2026
#Description: This program will calculate your BMI and how many weeks it will take to reach your goal weight.
Name = input("What is your name? ")
Height = float(input("What is your height in inches? "))
Weight = float(input("What is your weight in pounds? "))
Goal_Weight = float(input("What is your goal weight in pounds? "))
print("Name:", Name)
print("Height:", Height, "inches")
print("Weight:", Weight, "pounds")
print("Goal Weight:", Goal_Weight, "pounds")
print("Weight to lose:", Weight - Goal_Weight, "pounds")
print("BMI:", round((Weight / (Height ** 2)) * 703, 1))
print("weeks to lose weight:", round((Weight - Goal_Weight) / 1.5, 2), "weeks")