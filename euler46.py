from primes import primes

found = [] 
done = False

i = 1;
square_i = 0;
prime_i = 0;
square = 0
while not done:
    if i%1001==0:
        print i
    i+=2
    if i in primes or i in found:
        continue
    not_found = True
    while square <= i:
        p_sum = primes[prime_i]+square 
        print str(square_i)+":"+str(square)
        while p_sum<i:
            print ' '+str(prime_i)+":"+str(primes[prime_i])
            print '  '+str(p_sum)
            prime_i+=1
            p_sum = primes[prime_i]+square
            if p_sum not in found and not p_sum%2==0:
                found.append(p_sum)
        print ('--here--')
        if p_sum==i:
            found.append(p_sum)
            not_found = False
            break
        square_i +=1
        square = 2*square_i*square_i
        last_prime = prime_i-1
        prime_i=0
    if not_found:
        break
    if square>=i:
        square_i-=1
        square = 2*square_i*square_i
        prime_i = last_prime
print i
