def rotate(num):
	strnum = str(num)
	firstDigit = strnum[0]
	strnum = strnum[1:]
	strnum = strnum+firstDigit
	return int(strnum)

f = open('primes.txt','r')
primes = f.readlines()
for i in range(len(primes)):
	primes[i] = int(primes[i])
i = 0
count = 0;
while i<len(primes) and primes[i]<1000000:
	tisPrime = primes[i]
	lentis = len(str(tisPrime))
	isRotatable = True
	for rot in range(len(str(tisPrime))):
		tisPrime = rotate(tisPrime)
		if primes.count(tisPrime)>0 and len(str(tisPrime))==lentis:
			continue
		isRotatable = False
		break;
	if isRotatable:
		print(primes[i])
		count+=1
	i+=1
print(count)
