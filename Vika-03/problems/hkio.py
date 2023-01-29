numbers = input().split()

dic = {}

for value in numbers:
    if value in dic:
        dic[value] += 1
    else:
        dic[value] = 1
        
print(dic)

