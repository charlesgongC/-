# 二维数组中，每行从左到右递增，每列从上到下递增，给出一个数，判断它是否在数组中
def find_integer(matrix,num):
    if not matrix:
        return False
    rows,cols = len(matrix),len(matrix[0])
    row,col = rows -1 ,0
    while row >=0 and col <=cols -1:
        if matrix[row][col] == num:
            row -= 1
        elif matrix[row][col] >num:
            row -= 1
        else:
            col +=1
    return False