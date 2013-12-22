import copy
def read_in_sudoku_file(filename):
    f = open(filename)
    lines = [x.strip() for x in f.readlines()]
    grids = []
    for line in lines:
        if line[0:4] == 'Grid':
            try:
                grids.append(newGrid)
            except:
                pass
            newGrid = []
        else:
            newGrid.append(list(line))
    grids.append(newGrid)
    return grids

def solve_puzzle(grid):
    new_grid = fill_in(copy.deepcopy(grid))
    done = False
    while new_grid!=grid and not done:
        grid = new_grid
        new_grid = fill_in(copy.deepcopy(new_grid))
        if new_grid==False:
            return False
        done = is_done(new_grid)
    grid = new_grid
    if done:
        return grid

    for line_num, line in enumerate(grid):
        for row_num, item in enumerate(line):

            if item!='0':
                continue
            remaining = get_remaining(grid, line_num, row_num)
            if remaining==False:
                return False
            for option in remaining:
                pdb.set_trace()
                grid[line_num][row_num]=option
                new_grid = solve_puzzle(copy.deepcopy(grid))
                if new_grid==False:
                    continue 
                return new_grid
            return False

def is_done(grid):
    for line in grid:
        for item in line:
            if item=='0':
                return False
    return True

def get_remaining(grid, line_num, row_num):
    item = grid[line_num][row_num]
    if item!='0':
        return item 
    can_be = [str(i) for i in range(1,10)]
    for item_2 in grid[line_num]:
        try:
            del can_be[can_be.index(item_2)]
        except:
            pass
    if len(can_be)==1:
        return can_be[0]
    elif len(can_be)==0:
        return False
    row = [line[row_num] for line in grid]
    for item_2 in row:
        try:
            del can_be[can_be.index(item_2)]
        except:
            pass
    if len(can_be)==1:
        return can_be[0]
    elif len(can_be)==0:
        return False
    square_x_start = 0 if row_num<3 else 3 if row_num<6 else 6
    square_y_start = 0 if line_num<3 else 3 if line_num<6 else 6
    square = [line[square_x_start:square_x_start+3] for line in grid[square_y_start:square_y_start+3]]
    for square_row in square:
        for item_2 in square_row:
            try:
                del can_be[can_be.index(item_2)]
            except:
                pass
    if len(can_be)==0:
        return False
    return can_be


import pdb
def fill_in(grid):
    new_grid = copy.deepcopy(grid)
    for line_num, line in enumerate(grid):
        for row_num, item in enumerate(line):
            if grid[line_num][row_num]!='0':
                continue
            remaining = get_remaining(new_grid, line_num, row_num)
            if remaining==False:
                return False
            elif len(remaining)==1:
                new_grid[line_num][row_num]=remaining[0]
    return new_grid

if __name__=='__main__':
    puzzles = read_in_sudoku_file('sudoku.txt')
    solutions = []
    euler_answer = 0
    for i,puzzle in enumerate(puzzles):
        print i
        answer = solve_puzzle(puzzle)
        pdb.set_trace()
        
        solutions.append(answer)
        euler_answer+=int(''.join(answer[0][0:3]))
    print euler_answer
    
