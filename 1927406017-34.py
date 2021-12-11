n = int(input("please input a integer: "))
for i in range(1, n+1):
    print(" "*(n-i) + "*"*(2*i-1), end="")
    print("")


