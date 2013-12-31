from primes import primes

def isPalendrome(x):
    x = str(x)
    return x == x[::-1]
def toBinary(x):
    return bin(x)[2:]

def reduceFraction(num, den):
    prime_i = 0 
    while primes[prime_i]<=num and primes[prime_i]<=den:
        if num%primes[prime_i]==0 and den%primes[prime_i]==0:
            num/=primes[prime_i]
            den/=primes[prime_i]
        else:
            prime_i+=1

    return num, den
