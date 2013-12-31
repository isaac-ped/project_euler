import primes
weird_dens = []
weird_nums = []
for den in range(10,100):
    for num in range(10,den):
        str_den = str(den)
        str_num = str(num)
        found = False
        if str_den[0] in str_num and str_den[0]!='0':
            found = True
            new_den = str_den[1]
            if str_den[0]==str_num[0]:
                new_num = str_num[1]
            else:
                new_num = str_num[0]
        if str_den[1] in str_num and str_den[1]!='0':
            if found:
                found = False
                break
            found = True
            new_den = str_den[0]
            if str_den[1]==str_num[0]:
                new_num = str_num[1]
            else:
                new_num = str_num[0]
        if found and new_num!='0' and new_den!='0' and \
                float(num)/den==float(new_num)/float(new_den):
            weird_nums.append(num)
            weird_dens.append(den)
            print num,'/',den

total_num = 1
for num in weird_nums:
    total_num*=num
total_den = 1
for den in weird_dens:
    total_den*=den

import tools
new_num, new_den = tools.reduceFraction(total_num, total_den)

print total_num, total_den
print new_num, new_den

print float(total_num)/total_den
print float(new_num)/new_den
