# 7.	从键盘输入两个时间点，
# 格式hh:mm:ss（时：分：秒），计算两个时间点相隔的秒数，并输出。
import time
ti1 = time.strftime("15: 12: 13")
ti2 = time.strftime("16: 12: 13")
inter = (16*3600+12*60+13) - (15*3600+12*60+13)
print(inter)
