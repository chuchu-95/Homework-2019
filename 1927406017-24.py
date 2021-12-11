n = int(input("input an odd num: "))
row,col =0,n//2
mofang = []
for i in range(n):
    mofang.append([0]*n)
mofang[row][col]=1
for i in range(2,n*n+1):
    r,l = (row-1+n)%n,(col+1)%n
    if(mofang[r][l]==0):row,col =r,l
    else:row=(row+1)%n
    mofang[row][col]=i
t = len(str(n*n))
for i in mofang:
    for j in i:
        print("%-*d" %(t,j),end=" ")
    print("")
