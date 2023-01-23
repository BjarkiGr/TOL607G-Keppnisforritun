#line1 = input()
#line2 = input()
n = (int(input()))
temps = list(input().split())
count = 0

for i in range(n):
    if(int(temps[i]) < 0):
        count += 1

print(count)