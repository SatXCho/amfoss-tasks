manacount = 0

def debuff(levels):
    global manacount
    if (0 in levels):
        res = len([idx for idx, val in enumerate(levels) if val != 0])
        manacount+=res       
    elif(len(levels)==len(set(levels))):
        manacount+=1
        a = max(levels)
        b = min(levels)
        levels.remove(a)
        levels.append(b)
        debuff(levels)
    elif(len(levels)!=len(set(levels))):
        manacount+=1
        uniqlist = []
        for i in levels:
            if i not in uniqlist:
                uniqlist.append(i)
            else:
                levels.remove(i)
                break
        levels.append(0)
        debuff(levels)
        

    
    return manacount


t = int(input())
out = []

for i in range(t):
    n = int(input())
    levels = list(map(int,input().split()))
    ues = debuff(levels)
    manacount = 0
    out.append(ues)

print(*out, sep = "\n")
 
