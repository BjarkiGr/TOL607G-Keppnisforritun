n = int(input())
numbers = input().split()

numbersPrinted = 0
while numbers:
    maxValue = max(set(numbers), key=numbers.count)
    numbersPrinted += len(numbers)
    numbers = [x for x in numbers if x != maxValue]
    
print(numbersPrinted)
