# 8.请编写一个程序，产生两个[10，50]之间的随机数，
# 用这两个数构造一个复数，计算复数的模、辐角(要求转换成角度)，最后将复数、
# 复数的模和辐角显示在屏幕上。要求每个占7列，保留2位小数，右对齐。
import random
import cmath
m = random.uniform(10, 50)
n = random.uniform(10, 50)
fu1 = complex(m, n)
fu2 = complex(n, m)
a1, a2 = cmath.polar(fu1)
b1, b2 = cmath.polar(fu2)
print('复数1为：{0:7.2f}，模为{1:7.2f}，辐角为{2:7.2f}'.format(fu1, a1, a2))
print('复数2为：{0:7.2f}，模为{1:7.2f}，辐角为{2:7.2f}'.format(fu2, b1, b2))
