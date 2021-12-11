dec = eval(input("输入一个十进制正整数: "))
lst = []
while dec > 1:
    lst.append(dec%2)
    dec = dec//2
lst.append(dec)
for i in lst[::-1]:
    print(i,end="")



