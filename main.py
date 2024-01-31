import math
from cmu_graphics import *

def onAppStart(app):
    app.stepsPerSecond = 50
    app.width,app.height = 500,500
    app.weightInput = 'Type an expression'
    app.heightInput = 'Type an expression'
    app.sexInput = 'Type an expression'
    app.ageInput =  'Type an expression'
    app.loseWeight = False
    app.dropWeightlbs = None
    app.gainMuscle = False
    app.targetCalories = 0
    app.targetWeight = None
    app.calorieInput = None
    app.maintainWeight = False
    app.goal = None
    app.time = None
    app.BMR, app.BMI = None, None
    app.next1 = False
    app.next2 = False
    app.next3 = False
    app.mouseX, app.mouseY = 0,0
    app.color1,app.color2,app.color3 = "White","White", "White"
    app.counter = set()
    app.color = "White"
    L = ["AuBonPain", "Cucina","Grano","Nourish","Tepper Taqueria", "True Burger", "Urban Revolution"]
    app.preferences = set()
    app.ABP = False
    app.cucina = False
    app.grano = False
    app.nourish = False
    app.TT = False
    app.TB = False
    app.UR = False
    app.lowerCal = (app.targetCalories/3) - 50
    app.higherCal = (app.targetCalories/3) + 50
    app.calRange = (app.lowerCal, app.higherCal) #tuple
    app.results = calorieResults(app.lowerCal, app.higherCal, app.preferences) #dict
    app.cy = 50
    app.altResult = highestCal(preferences=None) #list

def BMRBMI(app):                                                                # added the rounded for bmi and bmr (see below), can remove if needed
    app.weightInput = float (app.weightInput)
    app.heightInput = float(app.heightInput)
    app.ageInput = float(app.ageInput)
    if app.sexInput.lower() == "m":
        bmr = rounded(66.47 + (13.75 * float(app.weightInput)) + (5.003 * float(app.heightInput)) - (6.755 * float(app.ageInput)))
        bmi = rounded((float(app.weightInput)/(float(app.heightInput/100)**2)))
        app.BMR = bmr
        app.BMI = bmi
        return (bmr, bmi)
    elif app.sexInput == "w":
        bmr = rounded(655.1 + (9.563 * app.weightInput) + (1.850 * app.heightInput) - (4.676 * app.ageInput))
        bmi = rounded((app.weightInput/((app.heightInput/100)**2)))
        return (bmr, bmi)
    else:
        return f"Please input the correct values and try again"
# def goals():
#     goal =  int(input("What are your goals for this app 1. To lose Weight 2. To maintain Weight 3. To gain Muscle: "))
#     if goal == 1:
#         return 1
#     if goal == 2:
#         return 2
#     if goal == 3:
#         return 3
#     else:
#         return goals()
def calories(app):      # changed checks, was previously checking goal == 1, 2, or 3, now checks goals == 0, 1, 2. (this is because you're setting goal as 0,1,2,... in your onMousePress)
    calorieInput = float(app.calorieInput)
    goal = app.goal    # also, this function isn't called anywhere, so app.dropWeightlbs isn't updated, which is why the label in the canvas says "...lose your target weight in None weeks"
    weightInput = app.weightInput
    targetWeight = app.targetWeight
    if goal == 0:
        targetCalories = calorieInput - 500
        print(targetCalories)
        # app.targetCalories = targetCalories
        print(f"app.targetCals: {app.targetCalories}")
        weightInput = float(app.weightInput)
        targetWeight = float(app.targetWeight)
        dropWeightlbs = (weightInput - targetWeight) / 2.20462
        print(f"weight Input:{weightInput}, dropWeightlbs:{dropWeightlbs}") 
        return math.floor(dropWeightlbs)

    elif goal == 1:
        maintainCalories = weightInput * 15
        return maintainCalories
    elif goal == 2:
        muscleCalories = 20 * (weightInput * 2.20462)
        return muscleCalories

def redrawAll(app):
    if app.next1 == False and app.next2 == False and app.next3 == False:
        drawLabel(f"Personal Info", app.width/2,50, align = "center", fill = "Purple", size = 30)
        drawLabel("Please fill in your info below and press enter after each value", app.width/2, 80, align = "center", size = 18)
        for i in range (6):
            drawRect(100, 145 + (i*50), 300, 30, fill = "White", border = "Black")
        drawLabel(f"Weight(Kg): {app.weightInput}", app.width/2, 160, align = "center", size = 16)
        drawLabel(f"Sex(M/F): {app.sexInput}", app.width/2, 210, align = "center", size = 16)
        drawLabel(f"Height(cm): {app.heightInput}", app.width/2, 260, align = "center", size = 16)
        drawLabel(f"Age: {app.ageInput}", app.width/2, 310, align = "center", size = 16)
        drawLabel(f"TargetWeight(kg): {app.targetWeight}", app.width/2,360,align = "center", size = 16)
        drawLabel(f"Current Calorie Intake(cal): {app.calorieInput}", app.width/2,410, align = "center", size = 16)
                # Arrows
        drawRect(425,450,25,25,fill = "Purple", border = "Black")
        drawPolygon(450,435,475,462.5,450,490, fill = "Purple", border = "Black")
        drawLabel("NEXT", 450,462.5, fill ="White", align = "center")

    elif app.next2 == False and app.next3 == False and app.next1 == True:
        drawLabel(f"WEIGHT GOALS", app.width/2,50, align = "center", fill = "Purple", size = 30)
        drawLabel("Please indicate your weight goals below.", app.width/2, 80, align = "center", size = 18)
        drawRect(app.width/5,150,25,25,fill =app.color1, border ="Black")
        drawLabel("Lose Weight",app.width/5 + 100,162.5, size = 16)
        drawRect(app.width/5,200,25,25,fill =app.color2, border ="Black")
        drawLabel("Build muscle Mass",app.width/5 + 100,212.5, size = 16)
        drawRect(app.width/5,250,25,25,fill =app.color3, border ="Black")
        drawLabel("Maintain Weight",app.width/5 + 100,265.5, size = 16)
        # Arrows
        drawRect(425,450,25,25,fill = "Purple", border = "Black")
        drawPolygon(450,435,475,462.5,450,490, fill = "Purple", border = "Black")
        drawLabel("NEXT", 450,462.5, fill ="White", align = "center")
        # Decorations
        drawCircle(0,0, 250, opacity = 25, fill = "Lightgreen")
        drawCircle(475,475,80, opacity = 25, fill = "Lightblue")
    elif app.next2 == True and app.next3 == False:
        drawLabel(f"Food Preferences", app.width/2,50, align = "center", fill = "Purple", size = 30)
        drawLabel(f"Click for Food Preferences or Next if None ", app.width/2, 75, align = "center", size = 16)
        L = ["AuBonPain", "Cucina","Grano","Nourish","Tepper Taqueria", "True Burger", "Urban Revolution"]
        counter = 0
        for i in range (len(L)):
            b = 100 + (i * 50)
            if i in app.counter:
                color = "Black"
                print(app.counter)
                print(app.preferences)
            else:
                color = "White"
            drawRect(app.width/5,b, 25,25,fill = color, border = "Black")
            drawLabel(f"{L[i]}", app.width/5 + 100,b + 12.5, size = 16 )
                # Arrows
        drawRect(425,450,25,25,fill = "Purple", border = "Black")
        drawPolygon(450,435,475,462.5,450,490, fill = "Purple", border = "Black")
        drawLabel("NEXT", 450,462.5, fill ="White", align = "center")  
    else:
        drawLabel(f"RESULTS", app.width/2,app.cy, align = "center", fill = "Purple", size = 30)
        drawLabel("Results: ", app.width/2, app.cy + 100, align = "center", fill = "Black", size = 20, bold = True)
        drawLabel(f"BMI: {app.BMI}", app.width/2, app.cy +130, align = "center", fill = "Black", size = 20)
        drawLabel(f"BMR: {app.BMR}", app.width/2, app.cy + 160, align = "center", fill = "Black", size = 20)
        targetcals = float(app.calorieInput) - 500
        drawLabel(f"Required Calorie Intake based on Goal: {targetcals}", app.width/2, app.cy + 190, align = "center", fill = "Black", size = 15)
        if app.goal == 0:
            dropWeight = calories(app)
            print(dropWeight)
            drawLabel(f"You would lose your target Weight in {dropWeight} weeks", app.width/2, app.cy + 220, size = 20)
        drawLabel(f"Your Personalized Meal Recommondations at CMU:", 
                    app.width/2, app.cy + 50, align = "center", fill = "Purple", size = 20)
        higher = ((float(app.calorieInput) -500) /3 ) + 50
        lower = ((float(app.calorieInput) -500) /3 ) - 50
        preferences = app.preferences
        results = calorieResults(lower, higher, preferences)
        L = results
        print(results)
        if (len(results) > 0):
            cy = app.cy
            cy = 300
            drawLabel(f"Restaurants: {app.preferences}", app.width/2, cy, size = 16, fill = "Purple", bold = True)
            for result in results:
                #L = results[result]
                cy += 20 
                #print restaurant name
                drawLabel((f"{result}"), app.width/2, cy, size = 16, fill = "Black")

        else: 
            drawLabel(f"There are no items that match you calorie requirement", 100, 35, size = 16, fill = "Blue")

def onMousePress(app, mouseX, mouseY):
    app.mouseX, app.mouseY = mouseX, mouseY
    print(f"mouseX:{app.mouseX}, mouseY:{app.mouseY}")
    i = getButtonPressed(app, mouseX, mouseY)
    if app.next1 == False and app.next2 == False and app.next3 == False:
        if i == 4:
            app.next1 = True
            BMRBMI(app)

    if app.next2 == False and app.next3 == False and app.next1 == True:
        if i == 0:
            app.loseWeight = True
            app.color1 ="Black"
            app.color2 ="White"
            app.color3 ="White"
            app.goal = 0
        elif i == 1:
            app.buildMuscle = True
            app.color1 ="White"
            app.color2 ="Black"
            app.color3 ="White"
            app.goal = 1
        elif i == 2:
            app.maintainWeight = True
            app.color1 ="White"
            app.color2 ="White"
            app.color3 ="Black"
            app.goal = 2
        elif i == 3:
            app.next2 = True
    elif app.next2 == True and app.next3 == False:
        L = ["AuBonPain", "Cucina","Grano","Nourish","Tepper Taqueria", "True Burger", "Urban Revolution"]
        if i == 0:
            app.ABP = True
            app.counter.add(i) if i not in app.counter else app.counter.remove(i)
            app.preferences.add(L[i]) if L[i] not in app.preferences else app.preferences.remove(L[i])

        elif i == 1:
            app.cucina = not app.cucina
            app.counter.add(i) if i not in app.counter else app.counter.remove(i)
            app.preferences.add(L[i]) if L[i] not in app.preferences else app.preferences.remove(L[i])
        elif i == 2:
            app.grano = not app.grano
            app.counter.add(i) if i not in app.counter else app.counter.remove(i)
            app.preferences.add(L[i]) if L[i] not in app.preferences else app.preferences.remove(L[i])
        elif i == 3:
            app.nourish = not app.nourish
            app.counter.add(i) if i not in app.counter else app.counter.remove(i)
            app.preferences.add(L[i]) if L[i] not in app.preferences else app.preferences.remove(L[i])
        elif i == 4:
            app.TT = not app.TT
            app.counter.add(i) if i not in app.counter else app.counter.remove(i)
            app.preferences.add(L[i]) if L[i] not in app.preferences else app.preferences.remove(L[i])
        elif i == 5:
            app.TB = not app.TB
            app.counter.add(i) if i not in app.counter else app.counter.remove(i)
            app.preferences.add(L[i]) if L[i] not in app.preferences else app.preferences.remove(L[i])
        elif i == 6:
            app.UR = not app.UR
            app.counter.add(i) if i not in app.counter else app.counter.remove(i)
            app.preferences.add(L[i]) if L[i] not in app.preferences else app.preferences.remove(L[i])
        elif i == 7:
            app.next3 = True
        

        

def getButtonPressed(app, mouseX, mouseY):
    if app.next1 == False and app.next2 == False and app.next3 == False:
        width = 100
        widthEnd = 400
        if mouseX >= width and mouseX <= widthEnd and mouseY >= 145 and mouseY <= 175:
            i = 0
            return i
        elif mouseX >= width and mouseX <= widthEnd and mouseY >= 195 and mouseY <= 225:
            i = 1
            return i
        elif mouseX >= width and mouseX <= widthEnd and mouseY >= 245 and mouseY <= 275:
            i = 2
            return i
        elif mouseX >= width and mouseX <= widthEnd and mouseY >= 295 and mouseY <= 325:
            i = 3
            return i
        elif mouseX >= width and mouseX <= widthEnd and mouseY >= 345 and mouseY <= 375:
            i = 5
            return i
        elif mouseX >= width and mouseX <= widthEnd and mouseY >= 395 and mouseY <= 425:
            i = 6
            return i
        elif mouseX >= 425 and mouseX <= 475 and mouseY >= 435 and mouseY <= 490:
            i = 4
            return i
        else:
            return
        

    if app.next2 == False and app.next1 == True and app.next3 == False:
        width = app.width/5
        widthEnd = width + 25
        if mouseX >= width and mouseX <= widthEnd and mouseY >= 150 and mouseY <= 175:
            i = 0
        elif mouseX >= width and mouseX <= widthEnd and mouseY >= 200 and mouseY <= 225:
            i = 1
        elif mouseX >= width and mouseX <= widthEnd and mouseY >= 250 and mouseY <= 275:
            i = 2
        elif mouseX >= 425 and mouseX <= 475 and mouseY >= 435 and mouseY <= 490:
            i = 3
        else:
            return
    else:
        width = app.width/5
        widthEnd = width + 25
        if mouseX >= width and mouseX <= widthEnd and mouseY >= 100 and mouseY <= 125:
            i = 0
        elif mouseX >= width and mouseX <= widthEnd and mouseY >= 150 and mouseY <= 175:
            i = 1
        elif mouseX >= width and mouseX <= widthEnd and mouseY >= 200 and mouseY <= 225:
            i = 2
        elif mouseX >= width and mouseX <= widthEnd and mouseY >= 250 and mouseY <= 275:
            i = 3
        elif mouseX >= width and mouseX <= widthEnd and mouseY >= 300 and mouseY <= 325:
            i = 4
        elif mouseX >= width and mouseX <= widthEnd and mouseY >= 350 and mouseY <= 375:
            i = 5
        elif mouseX >= width and mouseX <= widthEnd and mouseY >= 400 and mouseY <= 425:
            i = 6
        elif mouseX >= 425 and mouseX <= 475 and mouseY >= 435 and mouseY <= 490:
            i = 7
        else:
            return

    return i

def onKeyPress(app, key):
    if app.next1 == False:
        i = getButtonPressed(app,app.mouseX,app.mouseY)
        if i == 0:
            if app.weightInput == 'Type an expression':
                app.weightInput = ''
            if key.isdigit():
                if app.weightInput == 'Type an expression':
                    app.weightInput = ''
                app.weightInput += key
            if key == "backspace":
                temp = app.weightInput[0:-1]
                app.weightInput = temp
        if i == 1:
            if key.isalpha():
                if app.sexInput == 'Type an expression':
                    app.sexInput = ''
                app.sexInput += key
            if key == "backspace":
                temp = app.sexInput[0:-1]
                app.sexInput = temp
        if i == 2:
            if key.isdigit():
                if app.heightInput == 'Type an expression':
                    app.heightInput = ''
                app.heightInput += key
            if key == "backspace":
                temp = app.heightInput[0:-1]
                app.heightInput = temp
        if i == 3:
            if key.isdigit():
                if app.ageInput == 'Type an expression':
                    app.ageInput = ''
                app.ageInput += key
            if key == "backspace":
                temp = app.ageInput[0:-1]
                app.ageInput = temp
        if i == 5:
            if key.isdigit():
                if app.targetWeight == None:
                    app.targetWeight = ''
                app.targetWeight += key
            if key == "backspace":
                temp = app.targetWeight[0:-1]
                app.targetWeight = temp
        if i == 6:
            if key.isdigit():
                if app.calorieInput == None:
                    app.calorieInput = ''
                app.calorieInput += key
            if key == "backspace":
                temp = app.calorieInput[0:-1]
                app.calorieInput= temp

fileNames = ["AuBonPain.txt", "Cucina.txt", "Grano.txt", "Nourish.txt", 
             "TepperTaqueria.txt", "TrueBurger.txt", "UrbanRevolution.txt"]
restaurantNames = {}
for filename in fileNames: 
    d = {}
    with open(filename, encoding = 'utf-8') as f:
        for line in f:
            L = line.strip().split(',')
            key = L[0]
            val = L[1].strip()
            d[key] = int(val)
    index = filename.index(".")
    name = filename[:index]
    restaurantNames[name] = d
# print(restaurantNames)

def calorieResults(lower, higher, preferences):
    result = set()
    #if there is a preference, check only those restaurants
    if (preferences != None):
        for restaurant in restaurantNames:
            if restaurant not in preferences: 
                pass
            else: 
                itemDict = restaurantNames[restaurant]
                for item in itemDict:
                    cal = itemDict[item]
                    if (lower <= cal <= higher):
                        result.add((f"{restaurant}:", item, cal))
        print(result)
                    
    #if no preference, then check all
    # else: 
    #     for restaurant in restaurantNames:
    #         itemDict = restaurantNames[restaurant]
    #         for item in itemDict:
    #             cal = itemDict[item]
    #             if (lower <= cal <= higher):
    #                 result[restaurant] = [item, cal]
    return result
    #returns dict of place: [item, cal]

#this function is for when there are no results and need highest cal item (considering preferences)
#excluding this case
def highestCal(preferences=None):
    calDict = dict()
    calSet = set()
    #if there is a preference and finding max
    if (preferences != None):
        for restaurant in restaurantNames:
            if restaurant not in preferences: 
                pass
            else: 
                itemDict = restaurantNames[restaurant]
                for item in itemDict:
                    cal = itemDict[item]
                    #add to set
                    calDict[item] = [cal, restaurant]
                    calSet.add(cal)
    #if there is no preference just find max
    else:
        for restaurant in restaurantNames:
            itemDict = restaurantNames[restaurant]
            for item in itemDict:
                cal = itemDict[item]
                calDict[item] = [cal, restaurant]
                calSet.add(cal)
    #find max 
    maxCal = max(calSet)
    for item in calDict:
        if maxCal == calDict[item][0]:
            maxItem = item
            maxRestaurant = calDict[item][1]
    return ([maxRestaurant, maxItem, maxCal])




def main():
    runApp()

main()
