def get_matrix(n,m,value):
    matrix = []
    for i in range(n):
        row = []
        for j in range(m):
            row.append(value)
        matrix.append(row)
    return matrix

print(get_matrix(2,3,5))
print(get_matrix(3,4,6))
a = get_matrix(4,2,8)
print(a)
