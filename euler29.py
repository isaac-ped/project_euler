num_list = []
for i in range(2,101):
    for j in range(2,101):
        if pow(i,j) not in num_list:
            num_list.append(pow(i,j))
print len(num_list)
