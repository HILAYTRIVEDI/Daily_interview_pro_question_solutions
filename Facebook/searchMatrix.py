def searchMatrix(mat, value):
    result = False
    for i in mat:
        for j in i:
            if j == value:
                result = True
            else:
                continue
    return result


mat = [
    [1, 3, 5, 8],
    [10, 11, 15, 16],
    [24, 27, 30, 31],
]

print(searchMatrix(mat, 4))
# False

print(searchMatrix(mat, 10))
# True
