with open('RogovRomanNikolavich_UB32_vvod.txt', 'r') as file:

    lines = file.readlines()
    matrix = []

    for line in lines:
        row = line.strip().split(',')
        row = [element.strip('[]') for element in row]
        row = [int(element) if element else "" for element in row]
        matrix.append(row)

matrix = [list(filter(lambda x: x != '', row)) for row in matrix if row]
matrix = [x for x in matrix if x != []]


def find_max_ordered(matrix):
    max_element = 0
    for row in matrix:
        if sorted(row) == row or sorted(row, reverse=True) == row:
            current_max = max(row)
            if current_max > max_element:
                max_element = current_max

    return max_element


result = find_max_ordered(matrix)
with open("RogovRomanNikolavich_UB32_vivod.txt", "w") as file:
    file.write(str(result))