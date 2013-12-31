import itertools
permutations = list(itertools.permutations(range(1,10)))
products = []
def list2str(list_a):
    num = ''
    for i in range(len(list_a)):
        num+=str(list_a[i])
    return num
for p in permutations:
    p = list2str(p)
    for i in range(1,6):
        for j in range(i,10-i+2):
            if i>=j or j>=9:
                continue
            p1=int(p[0:i])
            p2=int(p[i:j])
            #print p
            #print [i,j
            p3=int(p[j:]) if j<9 else 0
            #print [p1,p2,p1*p2,p3]
            if p1*p2==p3:
                if p3 not in products:
                    print [p1,p2,p3]
                    products.append(p3)
print sum(products)
