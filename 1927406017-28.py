import math
x1, y1 = eval(input("input the center x1,y1: "))
r = eval(input("input radius: "))
x2, y2 = eval(input("please input x2,y2: "))
dis = math.sqrt((x1-x2)**2 + (y1-y2)**2)
if dis >= r:
    print("点在圆外")
else:
    print("点在圆内")
