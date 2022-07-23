#Import random

def matrixBuilder(num):
    rows_num = num
    columns_num = num
    matrix = []
    for i in range(rows_num):
        columns = []
        for j in range(columns_num):
            columns.append(1)
        matrix.append(columns)
    return matrix

print(matrixBuilder(3))