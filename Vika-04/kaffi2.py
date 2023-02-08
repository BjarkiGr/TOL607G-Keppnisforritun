colors, width = map(int, input().split())
chairs = list(map(int, input().split()))
amount = 0

for color in chairs:
    amount += color

lowerBound = 1
upperBound = 100000000

while (lowerBound < upperBound):
    middle = (lowerBound + upperBound)//2
    tmp = 0
    for i in range(colors):
        tmp += ((chairs[i] + middle - 1) // middle)
            
    if(tmp > width):
        lowerBound = middle + 1;
    else:
        upperBound = middle
	

print(width * lowerBound - amount);

