#enumerating source media for installable packages...
#d = {(1,1):1}
#possibilities = (1,2,5,10,20,50,100,200)
#def find_sum_to(value,max_index):
#    if (value,max_index) in d:
#        return d[(value,max_index)]
#    ways = 0
#    for i in range(0, max_index):
#        i2 =  possibilities[i];
#        while possibilities[i]<value-i2:
#            i-=1
#        ways += find_sum_to(value-i2,i)
#    d[(value,max_index)] = ways
#    return ways
#print 'starting'
#print find_sum_to(100,7)

poss = (200,100,50,20,10,5,2,1)
ways = []
global count
count = 0
def ways_to(value,sum_val, min_index):
    if sum_val<value:
        for i in range(min_index,len(poss)):
            ways_to(value,sum_val+poss[i],i)
    if sum_val==value:
        global count
        count+=1 
ways_to(200,0,0)
print count
