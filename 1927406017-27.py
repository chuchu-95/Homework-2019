import math
x1, x2, x3 = eval(input("please input x1,x2,x3: "))
y1, y2, y3 = eval(input("please input y1,y2,y3: "))
a = math.sqrt((x1-x2)**2 + (y1-y2)**2)
b = math.sqrt((x2-x3)**2 + (y2-y3)**2)
c = math.sqrt((x1-x3)**2 + (y1-y3)**2)
if a+b>c and a+c>b and b+c>a:
    zhouchang = a+b+c
    p = zhouchang/2
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    print("周长:%f, 面积:%f" %(zhouchang, s))
else:
    print("不能构成三角形!")


