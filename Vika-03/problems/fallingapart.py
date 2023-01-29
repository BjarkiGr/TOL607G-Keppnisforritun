n = int(input())
pieces = list(map(int, input().split()))

pieces.sort(reverse=True)

playerA = 0
playerB = 0

for i in range(n):
    if (i%2 == 0):
        playerA += pieces[i]
    else:
        playerB += pieces[i]

print(playerA, playerB)