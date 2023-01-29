n = int(input())
numbers = input().split()

dic = {}

for value in numbers:
    if value in dic:
        dic[value] += 1
    else:
        dic[value] = 1

numbers = list(dic.values())
numbers.sort(reverse=True)

sum = 0

for i in range(len(numbers)):
    sum += numbers[i] * (i+1)


print(sum)