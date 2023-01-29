from itertools import permutations

x = input()
numberArr = ([''.join(p) for p in permutations(x)])
higherNumbers = []


for i in range(len(numberArr)):
    if(x < numberArr[i]):
        higherNumbers.append(numberArr[i])

higherNumbers.sort()

if(len(higherNumbers) > 0):
    print(higherNumbers[0])
else:
    print(0)

