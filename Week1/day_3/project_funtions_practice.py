def calculate_bmi(weight, height_in_inches):
    """
    Calculate the Body Mass Index (BMI) based on weight and height.
    Parameters:
    weight (float): The weight of the individual in pounds.
    height_in_inches (float): The height of the individual in inches.
    Returns:
    float: The calculated BMI rounded to one decimal place.
    """
    bmi = (weight / (height_in_inches ** 2)) * 703
    return round(bmi, 1)
def convert_height_to_inches(feet, inches):
    """
    Convert height from feet and inches to total inches.
    Parameters:
    feet (int): The height in feet.
    inches (int): The additional height in inches.
    Returns:
    int: The total height in inches.
    """
    return (feet * 12) + inches
def bmi_category(bmi):
    """
    Determine the BMI category based on the calculated BMI.
    Parameters:
    bmi (float): The calculated Body Mass Index.
    Returns:
    str: The BMI category as a string.
    """
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
def fitness_report(weight, height_in_inches):
    bmi = calculate_bmi(weight, height_in_inches)
    category = bmi_category(bmi)
    print(f"current_BMI: {bmi}")
    print(f"category: {category}")
def goal_progress(current_weight, goal_weight):
    """
    Calculate the weight to lose and the estimated weeks to reach the goal weight.
    Parameters:
    current_weight (float): The current weight of the individual in pounds.
    goal_weight (float): The target weight of the individual in pounds.
    Returns:
    tuple: A tuple containing the weight to lose and the estimated weeks to reach the goal weight.
    """
    weight_to_lose = (current_weight - goal_weight)
    weeks_to_lose = round(weight_to_lose / 1.5, 2)  #Assuming a safe weight loss of 1.5 pounds per week
    print(f"Weight to Lose: {weight_to_lose} pounds")
    print(f"Estimated Weeks to Reach Goal: {weeks_to_lose}")
    print(f"Goal bmi: {calculate_bmi(goal_weight, height_in_inches)}")
def pounds_to_goal(current_weight, goal_weight):
    return current_weight - goal_weight
#"Stored Data" for calculations
current_weight = float(input("Enter your current weight in pounds: "))
goal_weight = float(input("Enter your goal weight in pounds: "))
height = input("What is your height? (ie, 6'3\"): ")
parts = height.split("'")
feet = int(parts[0])
inches = int(parts[1].rstrip('"'))
height_in_inches = convert_height_to_inches(feet, inches)
#User Report
print("="*30)
print("        Fitness Check-In")
print("="*30)
print("        User Profile")
print("-"*30)
print(f"name: John")
print(f"height: {height}")
print(f"current weight: {current_weight} pounds")
print("-"*30)
print("        Fitness Report")
print("-"*30)
fitness_report(current_weight, height_in_inches)
goal_progress(current_weight, goal_weight)