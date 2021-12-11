zheng = input("输入一个不多于 5 位的正整数: ")
if len(zheng) <= 5:
    print("它是%d位数"%(len(zheng)))
    lst = list(zheng)
    for i in lst:
        print(i)
    for i in lst[::-1]:
        print(i,end="")
else:
    print("输入有误,超过五位")

