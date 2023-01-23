line1 = input()
line2 = input()
n = (int(line1))
counting = list(line2.split())
errors = False

for i in range(1, n+1):
    if(counting[i-1]) == "mumble" or int((counting[i-1])) == i:
        errors = False
    else:
        errors = True

if(errors):
    print("something is fishy")
else:
    print("makes sense")