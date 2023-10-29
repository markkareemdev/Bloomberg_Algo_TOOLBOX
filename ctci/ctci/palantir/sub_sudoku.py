def sub_sudoku(matrix):
    #row
    for row in matrix:

        uniqueTable = [False for i in range(100000)]

        for i in row:
            if i < 1:
                return False
            if uniqueTable[i-1] == True:
                return False

            uniqueTable[i-1] = True

    #col
    for i in range(len(matrix)):

        uniqueTable = [False for i in range(100000)]

        for row in matrix:
            if row[i] < 1:
                return False
            if uniqueTable[row[i] - 1] == True:
                return False
            
            uniqueTable[row[i] - 1] = True
            # print(uniqueTable)


        
    return True
m = [[1, 3, 2],
[3, 1, 2],
[2, 3, 1]]

m1 = [[1, 2, 3],
[3, 1, 2],
[2, 3, 1]]

m2 = [[1000, -1000, 6],
[ 2, 3, 1],
[ 3, 1, 2]]



print(sub_sudoku(m))
print(sub_sudoku(m1))
print(sub_sudoku(m2))