import math

colors, width = map(int, input().split())
chairs = list(map(int, input().split()))
amount = 0

for color in chairs:
    amount += color


if(len(chairs) > width):
    whitespaces = width
else:
    height = math.ceil(amount/width)
    whitespaces = (width * height) - amount

print(whitespaces) 

# 5 23
# 21 14 24 7 17
