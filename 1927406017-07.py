from math import sqrt as q
(x1, y1) = eval(input("please input(x1, y1): "))
(x2, y2) = eval(input("please input(x2, y2): "))
(x3, y3) = eval(input("please input(x3, y3): "))
s1 = q((x1 - x2) ** 2 + (y1 - y2) ** 2)
s2 = q((x1 - x3) ** 2 + (y1 - y3) ** 2)
s3 = q((x2 - x3) ** 2 + (y2 - y3) ** 2)
s = (s1 + s2 + s3) / 2
area = q(s*(s-s1)*(s-s2)*(s-s3))
print("%-7.2f" % area)

