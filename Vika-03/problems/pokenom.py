battles = int(input()) # number of test cases T
results = []

for i in range(battles):
    rounds = int(input()) # number of rounds K
    results = []
    for i in range(rounds):
        results.append(input().split())

    A_points = 0 # Player A rounds won
    B_points = 0 # Player B rounds won
    steps = rounds * 2 # amount of steps, 2 per round

    Sth_step = 0 # number of steps where either player has won, regardless of remaining rounds
    Cth_step = 0 # number of steps where we know the remaining results, given we know S, A_points and B_points

    A_after_S = 0
    B_after_S = 0
    
    for i in range(rounds):
        if(results[i][0] == "E" and results[i][1] == "N"):
            A_points += 1
        elif(results[i][0] == "N" and results[i][1] == "E"):
            B_points += 1


        if(Sth_step == 0):
            if((A_points - B_points) > (rounds - (i+1))):
                Sth_step = ((i + 1) * 2) - 1
                A_after_S = A_points
                B_after_S = B_points
            elif((B_points - A_points) > (rounds - (i+1))):
                Sth_step = ((i + 1) * 2)
                A_after_S = A_points
                B_after_S = B_points
    
    winner = (max(A_after_S,B_after_S))

    Cth_step = (Sth_step - winner)

    print(Sth_step, Cth_step)
