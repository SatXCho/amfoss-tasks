
import math
def primeFactors(n):
	pf = []
	while n % 2 == 0:
		pf.append(2)
		n = n / 2
		
	for i in range(3,int(math.sqrt(n))+1,2):
		
		while n % i== 0:
			pf.append(i)
			n = n / i
			
	if n > 2:
		pf.append(n)

	return pf




monettt = list(map(int,input().split()))
monet = monettt[1]
t = monettt[0]
k = []
flag = 0
for i in range(1, monet + 1):
	if monet % i == 0 and i == t:
		flag = 1
		k.extend(primeFactors(monet//i))


 


if all(el == 2 or el == 3 for el in k) and flag == 1:
	print(len(k))
else:
	print(-1)
