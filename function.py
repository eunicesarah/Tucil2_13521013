# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
import math as m
import random
import os

os.system('cls')
print(" ██████╗██╗      ██████╗ ███████╗███████╗███████╗████████╗██████╗  █████╗ ██╗██████╗ ")
print("██╔════╝██║     ██╔═══██╗██╔════╝██╔════╝██╔════╝╚══██╔══╝██╔══██╗██╔══██╗██║██╔══██╗")
print("██║     ██║     ██║   ██║███████╗█████╗  ███████╗   ██║   ██████╔╝███████║██║██████╔╝")
print("██║     ██║     ██║   ██║╚════██║██╔══╝  ╚════██║   ██║   ██╔═══╝ ██╔══██║██║██╔══██╗")
print("╚██████╗███████╗╚██████╔╝███████║███████╗███████║   ██║   ██║     ██║  ██║██║██║  ██║")
print(" ╚═════╝╚══════╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝   ╚═╝   ╚═╝     ╚═╝  ╚═╝╚═╝╚═╝  ╚═╝")
print("=====================================================================================")
dot = int(input("Masukkan jumlah titik: "))
dim = int(input("Masukkan jumlah dimensi: "))

def random_matrix(dot, dim):
    matrix = [[0 for i in range(dim)] for j in range(dot)]
    # print(matrix)
    for i in range(dim):
        for j in range(dot):
            matrix[j][i] = random.randint(0, 100)
    # print(matrix)
    return matrix


def distance_matrix(matrix):
    dist_matrix = [[0 for i in range(dim)] for j in range(dim)]
    sum = 0
    # print(dist_matrix)
    for i in range(dim):
        for j in range(dim):
            dist_matrix[j][i] = (matrix[0][i] - matrix[1][i])**2
            
            # print(i, j)
        # print(dist_matrix[j][i])
        sum += dist_matrix[j][i]
    distance = m.sqrt(sum)
    # print(distance)
    return distance, matrix[0], matrix[1]
# distance_matrix(a)
a = random_matrix(dot, dim)

def sortX(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix)):
            if matrix[i][0] < matrix[j][0]:
                matrix[i], matrix[j] = matrix[j], matrix[i]
    # print(matrix)
    return matrix
