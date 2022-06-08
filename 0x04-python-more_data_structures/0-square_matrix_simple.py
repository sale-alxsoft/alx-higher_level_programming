#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    square = []
    for i in matrix:
        sub_list = []
        for j in i:
            sub_list.append(j)
        for x in range(len(i)):
            sub_list[x] = sub_list[x] ** 2
        square.append(sub_list)
    return (square)
