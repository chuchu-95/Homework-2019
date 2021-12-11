n = int(input("please input a integer: "))
print(" \t",end="")
for k in range(1, n+1):
    print("{0}\t".format(k), end="")
print("")
for i in range(1, n+1):
    print("{0}\t".format(i),end="")
    for j in range(1, i+1):
        print("{0}\t".format(i*j), end="")
    print("")
