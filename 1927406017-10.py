# 5.	请编写一个程序，产生一个在[5，20]之间的随机实数。
# 假设该随机数是一个球的半径，请计算该球的体积。
# 最后将球的半径和体积输出到屏幕上，要求每个值占15列，
# 保留3位小数，右对齐。
import random
from math import pi as p
r = random.uniform(5, 20)
V = 4 / 3 * (p * r ** 3)
print("%15.3f" % r)
print("%15.3f" % V)
