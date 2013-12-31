wordVals = [sum(ord(x)-ord('A')+1 for x in y) for y in open('words.txt').readline().replace('"','').split(',')]
def addTri():
    triVal = 0
    for i in range(100000):
        triVal += i 
        yield triVal
triVals=[0]
count = 0
triFunc = addTri();
for val in wordVals:
    while val>triVals[len(triVals)-1]:
        triVals.append(triFunc.next())
    if val in triVals:
        count+=1
print count
