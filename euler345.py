global matrix
matrix = [[int(y) for y in x.split()] for x in open('small_matrix.txt').readlines()]
global vals_taken
vals_taken = dict()
def sorted_xy(x,y):
    x,y = list(x),list(y)
    x.sort()
    y.sort()
    x,y = tuple(x),tuple(y)
    return (x,y)

def matrix_sum(used_x,used_y):
    global vals_taken
    sxy = sorted_xy(used_x,used_y)
    if sxy in vals_taken:
        return vals_taken[sxy]
    else:
        unused_x = []
        unused_y = []
        for x in range(len(matrix)):
            if x not in used_x:
                unused_x.append(x)
            if x not in used_y:
                unused_y.append(x)
        if len(unused_x)==0:
            return 0
        last_sum = 0
        this_xy = ()
        for x in unused_x:
            for y in unused_y:
                this_x = list(used_x)
                this_y = list(used_y)
                this_x.append(x)
                this_y.append(y)
                this_sum = matrix_sum(this_x,this_y)+matrix[x][y]
                if this_sum==matrix[x][y]:
                    print (this_x, this_y)
                    print this_sum
                if this_sum>last_sum:
                    last_sum = this_sum
        print sxy
        print this_sum
        vals_taken[sxy]=this_sum
        return this_sum
print vals_taken
print matrix_sum((),())
