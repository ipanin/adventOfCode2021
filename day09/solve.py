# Day 9: Smoke Basin 

import util
from collections import defaultdict

POS = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def solve1(data):
    matrix = []
    for line in data:
        row = [int(x) for x in line]
        matrix.append(row)
    W = len(matrix[0])
    H = len(matrix)
     
    sum = 0 
    for i,row in enumerate(matrix):
        for j,v in enumerate(row):
            found = True
            for di,dj in POS:
                i2 = i + di
                j2 = j + dj
                if 0 <= i2 < H and 0 <= j2 < W and matrix[i2][j2] <= v:
                    found = False
                    break;
            if found:
                sum += v+1
    return sum

def solve2(matrix):
    W = len(matrix[0])
    H = len(matrix)
     
    basins_sizes = []
    for i,row in enumerate(matrix):
        for j,v in enumerate(row):
            found = True
            for di,dj in POS:
                i2 = i + di
                j2 = j + dj
                if 0 <= i2 < H and 0 <= j2 < W and matrix[i2][j2] <= v:
                    found = False
                    break;
            if found:
                basins_sizes.append(calc_basin_size(matrix, i,j))
    a,b,c = sorted(basins_sizes, reverse=True)[0:3]
    return a*b*c

def calc_basin_size(matrix, i,j):
    map = defaultdict(int)
    map[(i,j)] = 1
    mark_near(map, matrix, i,j)
    return len(map)

def mark_near(map, matrix, i,j):
    W = len(matrix[0])
    H = len(matrix)
    for p in POS:
        i2 = i + p[0]
        j2 = j + p[1]
        if 0 <= i2 < H and 0 <= j2 < W and matrix[i2][j2] != 9 and map[(i2,j2)] == 0:
            map[(i,j)] = 1
            mark_near(map, matrix, i2, j2)

def test(filename, expected1, expected2):
    data = util.load_str_lines(filename)
    print(filename, "loaded")

    matrix = []
    for line in data:
        row = [int(x) for x in line]
        matrix.append(row)


    result = solve1(matrix)
    print("Part 1.", result)
    util.assert_equal(result, expected1)

    result = solve2(matrix)
    print("Part 2.", result)
    util.assert_equal(result, expected2)

test("input_sample.txt", 15, 1134)
test("input.txt", 580, 856716)