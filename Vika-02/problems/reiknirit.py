n = int(input())
numbers = input().split()

numbersPrinted = 0
numbers.sort()
numbers.insert(len(numbers), 0)


while(len(numbers) > 0):
    count = 0
    maxCount = 0
    location = 0
    numbersPrinted += len(numbers)-1
    for i in range(len(numbers) - 1):
        if(numbers[i] == numbers[i+1]):
            count += 1
        else:
            count = 0

        if(count >= maxCount):
            location = i+1
            maxCount = count

    if(maxCount == 0):
        numbers.pop()
        for m in range(0, len(numbers)):
            numbersPrinted += m
        numbers = []
        
    else:
        del(numbers[location-maxCount:location+1])
    
print(numbersPrinted)

