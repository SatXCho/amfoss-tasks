
nm = list(map(int,input().split()))
magic_dict = {}
out = []

for i in range(nm[1]):
    magic = list(map(str,input().split()))
    magic_dict[magic[0]] = magic[1]
harry_sloka = input()

def fastcast(dict,sloka):
    for magic_word in sloka.split():
        if len(magic_word)>len(dict[magic_word]):
            out.append(dict[magic_word])
        else:
            out.append(magic_word)


fastcast(magic_dict,harry_sloka)
print(*out)