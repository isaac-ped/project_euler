forward = dict()

def clean_dict(poss):
    items = poss.items()
    if len(items)==1:
        return poss
    i=0
    while not items[i][1][0] in poss:
        i+=1
    this_item = items[i][1].pop(0)
    next_item = poss[this_item].pop(0)
    if len(poss[this_item])==0:
        del poss[this_item]
    poss[items[i][0]].append(this_item+next_item)
    print '***************'
    for item in poss.items():
        print item
    return clean_dict(poss)

entries = [x for x in open('testkeylog.txt').readlines()]
for line in entries:
    if line in forward:
        continue
    if line[0] not in forward:
        forward[line[0]]=[line[1:3]]
    elif line[1:3] not in forward[line[0]]:
        forward[line[0]].append(line[1:3])
    if line[0:2] not in forward:
        forward[line[0:2]] = [line[2]]
    elif line[2] not in forward[line[0:2]]:
        forward[line[0:2]].append(line[2])
print clean_dict(forward)

    
