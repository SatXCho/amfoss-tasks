#portal 2 is a better game than god of war fight me

def portal(x,list):
    obtkeys = []
    obtkeys.append(x)
    obtkeys.append(list[x-1])
    obtkeys.append(list[obtkeys[1]-1])
    prod = 1
    for i in obtkeys:
        prod *= i
    if prod == 6:
        return "YES"
    else:
        return "NO"

t = int(input())
out = []
for i in range(t):
    x = int(input())
    abc = list(map(int,input().split()))
    out.append(portal(x,abc))

for i in out:
    print(i)

 
