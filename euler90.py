global required
required = {0:(1,4,6),1:(0,6),2:(5,),3:(6,),4:(0,6),5:(2,),6:(0,1,3,4),7:(),8:(1,)}
squares = (1,4,9,16,25,49,64,81)
def is_good(c1,c2):
    if 6 in c1:
        c1.append(9)
    if 6 in c2:
        c1.append(9)
    c1_10,c2_10 = [x*10 for x in c1],[x*10 for x in c2]
    possibilities = [x+y for x in c1 for y in c2_10]
    possibilities.extend([x+y for x in c2 for y in c2_10])
    return all([square in possiblities for square in squares])

def add_side(c1,c2,num):
    global required
    if num in c1:
        return (c1,c2)
    c1.append(num)
    print num
    for req in required[num]:
        if req not in c2:
            temp = add_side(c2, c1, req)
            print temp
            print str(c1) + '--'+str(c2)
            c1,c2 = temp[0], temp[1]

