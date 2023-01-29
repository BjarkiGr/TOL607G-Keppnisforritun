n = int(input())
numbers = input().split()

numbersPrinted = 0

while(numbers):
    dic = {}

    for value in numbers:
        if value in dic:
            dic[value] += 1
        else:
            dic[value] = 1
        
    maxCount = 0
    maxValue = 0

    for key, value in dic.items():
        if value >= maxCount:
            maxCount = value
            maxValue = key
    numbersPrinted += sum(dic.values())

    numbers = [x for x in numbers if x != maxValue]

print(numbersPrinted)