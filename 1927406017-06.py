# 从键盘输入一个3位整数，请编写程序
# 计算三位整数的各位数字之和，并输出到屏幕上，要求输出占4列，右对齐。
digit = 789
a = digit // 100
b = digit // 10 % 10
c = digit % 10
num1 = a + b + c
print("%d" % num1)
d = num1 // 10 % 10
e = num1 % 10
num2 = d + e
print("%2d" % num2)


