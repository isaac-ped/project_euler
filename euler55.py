non_lychrel = [1,2,3,4]
lychrel = []
def reverse(num):
    stnum=str(num)
    return int(stnum[::-1])

def isPalindrome(num):
    return str(num)[::-1]==str(num)

def isLychrel(num, iteration):
    if lychrel.count(num)==1:
        return True
    if iteration==50:
        lychrel.append(num)
        return True
    if non_lychrel.count(num)==1:
        return False
    if isPalindrome(num+reverse(num)):
        non_lychrel.append(num)
        return False
    if isLychrel(num+reverse(num),iteration+1):
        lychrel.append(num)
        return True
    else:
        return False
many = 0
for i in range(1,10000):
    if isLychrel(i,0):
        print i
        many+=1
print many
