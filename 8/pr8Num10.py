#10.1
def find_max_ordered(matrix):
    max_element = 0
    for row in matrix:
        if sorted(row) == row or sorted(row, reverse=True) == row:
            current_max = max(row)
            if current_max > max_element:
                max_element = current_max

    return max_element

matr = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [8, 7, 6, 5],
    [4, 3, 2, 1]
]

result = find_max_ordered(matr)
print(result)

#10.2
def sort_matrix_columns(matr):
    m = len(matr)  
    n = len(matr[0])  

    for j in range(n):  
        column = [matr[i][j] for i in range(m)] 
        sorted_column = sorted(column)  
        for i in range(m):  
            matr[i][j] = sorted_column[i]

    return matr


matr = [[5, 3], [9, 2], [4, 6]]
sorted_matrix = sort_matrix_columns(matr)
print(sorted_matrix)

