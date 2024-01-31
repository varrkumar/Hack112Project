from cmu_graphics import *


def BMRBMI():
    sexInput = input("What is your sex? M or F: ").lower()
    print(sexInput)
    weightInput = float(input("How much do you weigh in Kg?: "))
    heightInput = float(input("How tall are you in cm?: "))
    ageInput =  float(input("How old are you in years?: "))
    if sexInput == "m":
        bmr = rounded(66.47 + (13.75 * weightInput) + (5.003 * heightInput) -   #added rounded function here, can remove if needed
                      (6.755 * ageInput))
        bmi = rounded((weightInput/((heightInput/100)**2)))                     #added rounded
        return f'Your bmr is: {bmr}, and your bmi is: {bmi}'                    #edited print statement
    elif sexInput == "w":
        bmr = rounded(655.1 + (9.563 * weightInput) + (1.850 * heightInput) -   #added rounded
                      (4.676 * ageInput))
        bmi = rounded((weightInput/((heightInput/100)**2)))                     #added rounded
        return f'Your bmr is: {bmr}, and your bmi is: {bmi}'                    #edited for a nicer print (actual sentence, not just value)
    else:
        return f"Please input the correct values and try again"
def goals():                                                                    #edited the print statement in this function
    goal =  int(input("""
What are your goals for this app?
1. To lose Weight
2. To maintain Weight
3. To gain Muscle
"""))
    if goal == 1:
        return 1
    if goal == 2:
        return 2
    if goal == 3:
        return 3
    else:
        return goals()
def calories():                                                                 #edited prints in this func
    calorieInput = float(input("""
On average how many calories do you consume on a daily basis ?:
"""))
    goal = goals()
    if goal == 1:
        targetCalories = calorieInput - 500
        weightInput = float(input("How much do you weigh in Kg?: "))
        targetWeight = float(input(
            "What is your target weight in kilograms?: "))
        dropWeightlbs = (weightInput - targetWeight) * 2.20462
        message = print(
            f"""
If you consume {targetCalories} calories a day, 
you would lose you desired weight in {dropWeightlbs} weeks
""")
        return message
    elif goal == 2:
        weightInput = float(input("How much do you weigh in Kg?: "))
        maintainCalories = weightInput * 15                                     # not sure about the logic here, also added 'weightInput' on line above again
        message = f"""
You need to consume approximately
{maintainCalories} calories a day to maintain your current weight
"""
        return message
    elif goal == 3:
        muscleCalories = 20 * (weightInput * 2.20462)
        message = f"""
To build muscle, you need to consume approximately {muscleCalories} calories
a day, coupled with the appropriate exercise
"""
        return message
    




def onappStart(app):  
    app.width, app.height = 1500,1500
def redrawAll(app):
    pass

def main():
    # print(BMRBMI())
    # print(goals())
    print(calories())
    runApp()

main()
