#10.1
def find_max_ordered(matrix):
    max_element = 0

    # Перебираем каждую строку матрицы
    for row in matrix:
        # Проверяем, является ли строка упорядоченной
        if sorted(row) == row or sorted(row, reverse=True) == row:
            # Находим максимальный элемент в упорядоченной строке
            current_max = max(row)
            # Обновляем максимальный элемент, если текущий больше
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
print(result)  # Выведет: 8

#10.2
def sort_matrix_columns(matr):
    m = len(matr)  # количество строк
    n = len(matr[0])  # количество столбцов

    for j in range(n):  # для каждого столбца матрицы
        column = [matr[i][j] for i in range(m)]  # создаем список из элементов столбца
        sorted_column = sorted(column)  # сортируем список элементов столбца
        for i in range(m):  # заменяем элементы столбца отсортированными значениями
            matr[i][j] = sorted_column[i]

    return matr


matr = [[5, 3], [9, 2], [4, 6]]
sorted_matrix = sort_matrix_columns(matr)
print(sorted_matrix)

