a,n = eval(input("please input a,n: "))
s = 0
for i in range(1,n+1):
    m = eval("{}".format(a)*i)
    s += m
print(s)
