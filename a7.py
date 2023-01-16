import sys
from math import trunc
import numpy as np


def main():
    mat1 = np.loadtxt("matrix1-2.txt", dtype='i', delimiter=' ')
    mat2 = np.loadtxt("matrix2-2.txt", dtype='i', delimiter=' ')
    final = []

    if (100 > len(mat1) > 1) and (100 > len(mat2) > 1):
        final = np.matmul(mat1, mat2)
        print(final)
        np.savetxt('testout.txt', final, fmt='%d', delimiter=' ')

    else:
        print("Error: Wrong Size")


main()
