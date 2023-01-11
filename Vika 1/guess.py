
firstGuess = 500
print(firstGuess)

for i in range(1, 11):
    answer = input()
    if(answer == "lower"):
        guess = guess / 2
        print(round(guess))
    elif(answer == "higher"):
        guess = guess * 1.5
        print(round(guess))
    else:
        break
