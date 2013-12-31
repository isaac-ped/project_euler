#enumerating source media for installable packages...
d = {(0,0):1}
def find_sum_to(value,maximum):
    if (value,maximum) in d:
        return d[(value,maximum)]
    ways = 0
    for i in range(1, maximum+1):
        ways += find_sum_to(value-i,i if i<value-i else value-i)
    d[(value,maximum)] = ways
    return ways
print 'starting'
print find_sum_to(100,99)
