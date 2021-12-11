a, b, c = eval(input("please input a,b,c: "))
from math import sqrt as q
if a == 0:
    print("错，a不能为0")
else:
    delta = b**2 - 4*a*c
    if delta >= 0:
        x1 = (-b + q(delta)) / 2*a
        x2 = (-b - q(delta)) / 2*a
    else:
        x1 = complex((-b)/(2*a), q(-delta)/2*a)
        x2 = complex((-b)/(2*a), q(-delta)/2*a)
    print("{:10.5f},{:10.5f}".format(x1, x2))




