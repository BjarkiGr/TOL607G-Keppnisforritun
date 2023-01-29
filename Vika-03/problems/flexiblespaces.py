width, partitions = list(map(int, input().split()))
locations = list(map(int, input().split()))

outcomes = [width]


for i in range(len(locations)):
    outcomes.append(locations[i])
    outcomes.append(width - locations[i])
    for j in range(len(locations)):
        if(locations[j] > locations[i]):
            outcomes.append(locations[j] - locations[i])

outcomes.sort()
outcomes = list(dict.fromkeys(outcomes))   

for outcome in outcomes:
    print(outcome)