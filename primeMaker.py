f = open('primes.txt', 'w')
primes = [2]
f.write('2\n') 
for i in range(3,1000000,2):
	isprime = True
	for prime in primes:
		if i%prime==0:
			isprime = False
			break
	if isprime:
		primes.append(i)
		f.write(str(i)+"\n")
f.close()


