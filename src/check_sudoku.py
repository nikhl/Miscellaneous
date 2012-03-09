correct2 = [[3,4,1,2,5], [1,3,4,5,2], [4,5,2,3,1], [2,1,5,4,3], [5,2,3,1,4]]

incorrect2 = [[1,2,3,4], [4,3,2,1], [3,1,4,2], [2,4,3,1]]

incorrect3 = [[1,2,3], [2,3,1], [3,1,5]]

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]

incorrect = [[1,2,3,4],
             [2,3,1,3],
             [3,1,2,3],
             [4,4,4,4]]

# Returns whether the given list is unique or not
def is_unique(list,range):
    for each in list:
        if each > range:
            return False
    return len(list) == len(set(list))

# Checks whether the given square(nxn) list of lists forms sudoku square or not
def check_sudoku(square):
    size = len(square[0])
    
    # checking row wise uniqueness
    for i in range(size):
        if not (is_unique(square[i],size)):
            return False

    # Checking column wise uniqueness
    for i in range(size):
        column = []
        for j in range(size):
            column.append(square[j][i])
        if not is_unique(column,size) :
            return False
    return True
    




print check_sudoku(correct) 
