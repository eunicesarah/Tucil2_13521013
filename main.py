from function import *
import time as t

def divide(matrix):
    # left = []
    # right = []
    if len(matrix) % 2 == 0:
        mid = len(matrix) // 2
        left = matrix[:mid]
        right = matrix[mid:]
    else:
        mid = len(matrix) // 2
        left = matrix[:mid]
        right = matrix[mid+1:]
        # left.append(l)
        # right.append(r)
        # return min(divide(left), divide(right))
    # print("Left: ", left)
    # print("Right: ", right)
    return left, right

def bruteForce(matrix):
    dmin = 9999
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            d = distance_matrix([matrix[i], matrix[j]])
            if d < dmin:
                dmin = d
    # print("terkecil : ", dmin)
    return dmin


def sStrip(matrix, distance):
    if len(matrix) % 2 == 0:
        mid = len(matrix) // 2
        strip = (matrix[mid+1:] + matrix[mid:]) // 2
    else:
        mid = len(matrix) // 2
        strip = matrix[mid:]
    
    min = distance
    for i in range(len(strip)):
        for j in range(i+1, len(strip)):
            if strip[j][1] - strip[i][1] < min:
                d = distance_matrix([strip[i], strip[j]])
                return d

    

def closestPair(matrix,dot):
    # t.sleep(1)
    if len(matrix) == 2:
        distance = distance_matrix(matrix)
    elif len(matrix) == 3:
        distance = bruteForce(matrix)
    else:
        left, right = divide(sortX(matrix))
        # print(left)
        # print(right)
        dl = closestPair(left, len(matrix)//2)
        print(dl)
        dr = closestPair(right, len(matrix)//2)
        print(dr)
        distance = min(dl, dr)
        # sStrip(sortX(matrix), distance)
    return distance
# distance_matrix(a)
z = closestPair(a, dot)
print("jadi", z)
