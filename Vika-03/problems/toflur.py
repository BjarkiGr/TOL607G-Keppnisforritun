tiles = int(input())
numbers = list(map(int, input().split()))
numbers.sort()
score = 0

for i in range(len(numbers)-1):
    score += (int(numbers[i]) - int(numbers[i+1]))**2

print(score)