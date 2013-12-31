from primes import primes
total_sum = 0
def truncatable_left(val):
    val = str(val)
    if '0' in val or '4' in val or '6' in val or '8' in val:
        return False
    while len(val)>0:
        if not int(val) in primes:
            return False
        val = val[:len(val)-1]
    return True

def truncatable_right(val):
    val = str(val)
    if  '0' in val or '4' in val or '6' in val or '8' in val:
        return False
    while len(val)>0:
        if not int(val) in primes:
            return False
        val = val[1:len(val)]
    return True

def go():
    total_sum = 0
    for prime in primes:
        if prime in (2,3,5,7):
            continue
        if truncatable_left(prime) and truncatable_right(prime):
            total_sum+=prime
            print "----"+str(prime)
            print "="+str(total_sum)
go()
