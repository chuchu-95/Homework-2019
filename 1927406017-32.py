pro = eval(input("please input the num of money: "))
if pro<100000:
    print(pro*1.015)
elif pro>=100000 and pro<500000:
    print(pro*1.02)
elif pro>=500000 and pro<1000000:
    print(pro*1.03)
else:
    print(pro*1.035)
