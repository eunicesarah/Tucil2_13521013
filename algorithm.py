from function import *
import time as t

count = 0

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
    global count
    dmin = 9999
    A = []
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            d = distance_matrix([matrix[i], matrix[j]])
            # count += 1
            if d[0] < dmin:
                dmin = d[0]
                A = d[1], d[2]
    # print("terkecil : ", dmin)
    return dmin, A   


def sStrip(matrix, distance):
    global count
    terjauh = matrix[len(matrix)-1][0] - matrix[0][0]/2
    for i in range(len(matrix)):
        for j in range(i+1, len(matrix)):
            # if matrix[j][0] - matrix[i][0] < terjauh:
                d = distance_matrix([matrix[i], matrix[j]])
                count += 1
                if d[0] < distance:
                    return d[0], d[1], d[2]
    return distance, matrix[0], matrix[1]

    

def closestPair(matrix,dot):
    # t.sleep(1)
    global count
    if len(matrix) == 2:
        distance, point1, point2 = distance_matrix(matrix)
        count += 1
        # print("matrix terdekat adalah dist", point1, "dan", point2, "dengan jarak", distance)
        return distance, point1, point2

    elif len(matrix) == 3:
        distance, A = bruteForce(matrix)
        point1 = A[0]
        point2 = A[1]
        # print("matrix terdekat adalah brute", point1, "dan", point2, "dengan jarak", distance)
        return distance, point1, point2
    else:
        left, right = divide(sortX(matrix))
        # print(left)
        # print(right)
        dl = closestPair(left, len(matrix)//2)
        # print(dl)
        point11, point21 = left[0], left[1]
        dr = closestPair(right, len(matrix)//2)
        # print(dr)
        point12, point22 = right[0], right[1]
        if dl < dr :
            point1 = point11
            point2 = point21
        else:
            point1 = point12
            point2 = point22
        distance = min(dl, dr)[0]
        # print("distance: ", distance)
        minimum, point13, point23 = sStrip(matrix, distance)
        # print("sStrip: ", minimum)
        if minimum < distance:
            distance = minimum
            point1 = point13
            point2 = point23
            # print("matrix terdekat adalah minimum", point1, "dan", point2, "dengan jarak", distance)
            return distance, point1, point2
        else:
            point1 = min(dl, dr)[1]
            point2 = min(dl, dr)[2]
            # print("matrix terdekat adalah distance", point1, "dan", point2, "dengan jarak", distance)

            return distance, point1, point2
    # return distance, point1, point2
# distance_matrix(a)

# print("halo: ", sStrip(a, distance_matrix(a)[0]))

def main():
    startTime = t.time()
    z, b, c = closestPair(a, dot)
    endTime = t.time()
    print("================================DIVIDE AND CONQUER===================================")
    print("Jarak terdekat: ", z)
    print("Pasangan titik terdekat: ", b, c,)
    print("Banyak Euclidean Distance yang dihitung: ", count, "kali")
    print("Execution time: ", endTime - startTime, "detik")
    print("====================================BRUTE FORCE======================================")
    startTimeBrute = t.time()
    d, e = bruteForce(a)
    endTimeBrute = t.time()
    print("Jarak terdekat: ", d)
    print("Pasangan titik terdekat: ", e)
    print("Execution time: ", endTimeBrute - startTimeBrute, "detik")

main()