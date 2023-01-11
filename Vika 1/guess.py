low = 0
high = 1000
guess = (low + high) // 2
print(guess)

for i in range(1, 11):
    answer = input()
    if(answer == "lower"):
        high = guess
        guess = (low + high) // 2
        print(guess)

    elif(answer == "higher"):
        low = guess
        guess = (low + high + 1) // 2
        print(guess)

    elif(answer == "correct"):
        break
