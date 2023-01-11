# Keppnisforritun - Vika 1
## Bjarki Grettisson

Í þessari viku var farið yfir hvernig námskeiðinu verður háttað, og aðeins skoðað open.kattis.com\
Fyrsta heimaverkefnið var gefið út.


# Dæmablað 1

| Dæmi | ID | stig |
| Hello World | hello | 1 |

| Dæmi | ID | Stig |
| ----------- | ----------- | ----------- |
| Hello World | hello | 1 |
| Sort Two Numbers | sort | 1 |
| Quadrant Selection | quadrant | 1 |
| Cold-puter Science | cold | 1 |
| Baby Bites | babybites | 1 |
| Guess the Number | guess | 2 |

## Mínar lausnir

hello.py
```
print("Hello World!")
```

sort.py
```
line = input()
a, b = map(int, line.split())

if(a < b):
    print(a, b)
else: 
    print(b, a)
```

quadrant.py
```
line1 = input()
line2 = input()
x, y = map(int, (line1, line2))

if(x > 0):
    if(y > 0):
        print(1)
    else:
        print(4)
else:
    if(y > 0):
        print(2)
    else:
        print(3)
        
```

cold.py
```
#line1 = input()
#line2 = input()
n = (int(input()))
temps = list(input().split())
count = 0

for i in range(n):
    if(int(temps[i]) < 0):
        count += 1

print(count)
```

babybites.py
```
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
```

guess.py
```


```