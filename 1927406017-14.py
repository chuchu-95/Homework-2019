 # 请计算当前距离1970年1月1日过去了多少天又多少小时，并输出到屏幕上。
import time
times = int(time.time())
second = times % 60
hours = times // 3600
minutes = (times - hours * 3600) // 60
days = hours // 24
hours = hours - days * 24
print("从1970年到现在过去了", "%d 天,%d 小时,%d 分,%d 秒" %(days, hours, minutes, second))
