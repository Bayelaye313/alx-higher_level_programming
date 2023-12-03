#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for i, row in enumerate(matrix):
        for j, element in enumerate(row):
            print("{:d}".format(matrix(element)), end="")
            if j != (len(row) - 1):
                print(" ", end="")
        print("")
