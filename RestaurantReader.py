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

def calorieResults(lower, higher, preferences=None):
    result = {}
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
                        result[restaurant] = [item, cal]
                    
    #if no preference, then check all
    else: 
        for restaurant in restaurantNames:
            itemDict = restaurantNames[restaurant]
            for item in itemDict:
                cal = itemDict[item]
                if (lower <= cal <= higher):
                    result[restaurant] = [item, cal]
    return result
    #returns dict of place: [item, cal]

#this function is for when there are no results and need highest cal item (considering preferences)
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
    #test cases
    print(calorieResults(400, 1100))
    print(highestCal(preferences="Nourish"))
main()
