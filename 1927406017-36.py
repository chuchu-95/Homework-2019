n = int(input("please input a integer: "))
for i in range(1, 2*n):
    for j in range(abs(i-n)):
        print("  ", end="")
    for j in range(2*n-1-abs(i-n)):
        print("*  ", end=" ")
    print()


