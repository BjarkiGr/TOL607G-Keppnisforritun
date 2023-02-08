blocks = int(input()) 
towers = list(map(int, input().split())) 

minCharges = blocks

towers.sort(reverse=True)

for i in range(blocks):
    if((i + towers[i]) < minCharges):
        minCharges = i + towers[i]


print(minCharges)
