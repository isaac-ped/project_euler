from tools import isPalendrome, toBinary
n_sum = 0
for i in range(1000000):
    if isPalendrome(i) and isPalendrome(toBinary(i)):
        n_sum += i
        print i
print n_sum
