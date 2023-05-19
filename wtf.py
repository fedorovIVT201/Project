# 7 1 3 -2 0
# 0 10 -4 3 10
# -1 1 5 2 -2
# 2 4 -1 6 15
matrix = [[4, 1, 2, 0.5, 2],
[1, 0.5, 0, 0, 0],
[2, 0, 3, 0, 0],
[0.5, 0, 0, 0.625, 0],
[2, 0, 0, 0, 16]]

mat = []
l = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
a = 0
# for i in range(5):
#     line = input()
#     row = [float(s) for s in line.split()]
#     matrix.append(row)
# for i in range(len(matrix)):
#     for j in range(len(matrix[0])):
#         print(matrix[i][j], end=" ")
#     print()
# for i in range(len(matrix)):
#     if matrix[i][0]==1 or matrix[i][0]==-1:
#         mat = matrix[0]
#         matrix[0] = matrix[i]
#         matrix[i] = mat
# for i in range(len(matrix)):
#     if matrix[i][0] == 0:
#         mat = matrix[i]
#         matrix[i] = matrix[len(matrix)-1-a]
#         matrix[len(matrix)-1-a] = mat
#         a += 1
# for i in range(len(matrix)-1):
#     if matrix[i+1][0] != 0:
for j in range(0, 5):
    k = 0
    summa = 0
    while k <= j-1:
        proiz = l[j][k]*l[j][k]
        summa += proiz
        k += 1
    l[j][j] = (matrix[j][j]-summa)**(1/2)
    for i in range(j+1, 5):
        k = 0
        summ = 0
        while k <= i - 1:
            proiz = l[i][k]*l[j][k]
            summ += proiz
            k += 1
        l[i][j] = (matrix[i][j] - summ)/l[j][j]

lt = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]

for i in range(len(l)):
    for j in range(len(l[0])):
        lt[i][j] = l[j][i]
print("==================")
for i in range(len(l)):
    for j in range(len(l[0])):
        print(lt[i][j], end=" ")
    print()
y = [0,0,0,0,0]
x = [0,0,0,0,0]
b = [7,3,7,-4,-4]

for i in range(0, 5):
    k = 0
    summak = 0
    while k <= i-1:
        proiz = l[i][k] * y[k]
        summak += proiz
        k += 1
    y[i] = (b[i]-summak)/l[i][i]
print("=================")
for i in range(5):
    print(y[i], end=" ")

for i in range(4, -1, -1):
    k = 4
    summal = 0
    while k >= i+1:
        summal += lt[i][k]*x[k]
        k -= 1
    x[i] = (y[i]-summal)/lt[i][i]
# y1 = b[0]/l[0][0]
# y2 = b[1]/(l[1][1]+l[1][0])
# y3 = b[2]/(l[2][2]+l[2][1]+l[2][0])
# y4 = 0
# y5 = b[4]/(l[4][4]+l[4][3]+l[4][2]+l[4][1]+l[4][0])

# x1 = y[0]/(lt[0][0]+lt[0][1]+lt[0][2]+lt[0][3]+lt[0][4])
# x2 = y[1]/(lt[1][1]+lt[1][2]+lt[1][3]+lt[1][4])
# x3 = y[2]/(lt[2][2]+lt[2][3]+lt[2][4])
# x4 = y[3]/(lt[3][3]+lt[3][4])
# x5 = y[4]/lt[4][4]
# for i in range(4):
#     for j in range(i+1, 4):
#         kof = matrix[j][i]/matrix[i][i]
#         for k in range(i, 4):
#             matrix[j][k] = matrix[j][k] - matrix[i][k]*kof
#             matrix[j][4] = matrix[j][4] - matrix[i][4]*kof
for i in range(len(l)):
    for j in range(len(l[0])):
        print(l[i][j], end=" ")
    print()
# x4 = matrix[3][4]/matrix[3][3]
# x3 = matrix[2][4]/(matrix[2][2]+x4)
# x2 = matrix[1][4]/(matrix[1][1]+x3+x4)
# x1 = matrix[0][4]/(matrix[0][0]+x2+x3+x4)
print(x[0], " ", x[1], " ", x[2], " ", x[3], " ", x[4])