while True:
    n = int(input("please input a integer: "))
    if type(n) != int:
        print("当前的输入非法需要重新输入数值")
    if n != 0:
        sum = 0
        for j in range(1,n+1):
            k = eval(input("Please input number %d: " % (j)))
            sum += k
        print(sum)



