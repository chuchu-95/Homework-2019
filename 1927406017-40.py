n = int(input("Please input the number of rows: "))
m = int(input("Please input the number of columns: "))
A = []
B = []
C = []
for i in range(n):
    A.append([0]*m)
    B.append([0]*m)
    C.append([0]*m)
for j in range(n):
    for h in range(m):
        print("please input A[{},{}]:".format(j,h),end="")
        A[j][h] = eval(input())
for j in range(n):
    for h in range(m):
        print("please input B[{},{}]:".format(j,h),end="")
        B[j][h] = eval(input())
for j in range(n):
    for h in range(m):
        C[j][h] = A[j][h] + B[j][h]
print(C)

