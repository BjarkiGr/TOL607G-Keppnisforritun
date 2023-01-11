line1 = input()
line2 = input()
n = (int(line1))
counting = list(line2.split())
errors = 0

for i in range(1, n+1):
    if(counting[i-1]) == "mumble" or int((counting[i-1])) == i:
        errors += 0
    else: 
        errors += 1

if(errors > 0):
    print("something is fishy")
else:
    print("makes sense")