def fitness_summary(weight, height_in_inches):

    bmi = calculate_bmi(weight, height_in_inches)
    category = bmi_category(bmi)

    return bmi, category

def calculate_bmi(weight, height_in_inches):
    bmi = (weight / (height_in_inches ** 2)) * 703
    return round(bmi, 1)
def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

bmi, category = fitness_summary(200, 75)

print(bmi)
print(category)