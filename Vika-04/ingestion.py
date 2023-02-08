import math

courses, maxCaloriesPerHour = map(int, input().split())
caloriesPerCourse = list(map(int, input().split()))

maxCal = maxCaloriesPerHour

eatenCalories = 0
caloriesPerCourse.append(0)
caloriesPerCourse.append(0)

for i in range(courses):
    if(caloriesPerCourse[i] >= maxCaloriesPerHour):
        eatenCalories += maxCaloriesPerHour
        print("Choice 1, ate", maxCaloriesPerHour, "in course", i+1)
        maxCaloriesPerHour = math.trunc(maxCaloriesPerHour*(2/3))
        print("new maxCalories:", maxCaloriesPerHour)
    
    else:
        if(caloriesPerCourse[i] < caloriesPerCourse[i+1]):
            eatenCalories += 0
            print("Choice 2, ate nothing in course", i+1)
            maxCaloriesPerHour = math.trunc(maxCaloriesPerHour*(3/2))
            if(maxCal < maxCaloriesPerHour):
                maxCaloriesPerHour = maxCal
            print("new maxCalories:", maxCaloriesPerHour)

        elif(caloriesPerCourse[i+1] >= math.trunc((maxCaloriesPerHour*(3/2)))):
            eatenCalories += 0
            print("Choice 2, ate nothing in course", i+1)
            maxCaloriesPerHour = math.trunc(maxCaloriesPerHour*(3/2))
            if(maxCal < maxCaloriesPerHour):
                maxCaloriesPerHour = maxCal
            print("new maxCalories:", maxCaloriesPerHour)

        elif(caloriesPerCourse[i+1] > caloriesPerCourse[i] and caloriesPerCourse[i+2] > math.trunc(math.trunc((maxCaloriesPerHour*(3/2)))*(3/2))):
            eatenCalories += 0
            print("Choice 3, ate nothing in course", i+1)
            maxCaloriesPerHour = math.trunc(maxCaloriesPerHour*(3/2))
            if(maxCal < maxCaloriesPerHour):
                maxCaloriesPerHour = maxCal
            print("new maxCalories:", maxCaloriesPerHour)

        else:
            eatenCalories += caloriesPerCourse[i]
            print("Choice 4, ate", caloriesPerCourse[i], "in course", i+1)
            maxCaloriesPerHour = math.trunc(maxCaloriesPerHour*(2/3))
            print("new maxCalories:", maxCaloriesPerHour)
           


print(eatenCalories)
