n = int(input("please input n: "))
count = 0
while n != 0:
    if n >= 75:
        n -= 75
        count += 7
        continue
    if n >= 45 and n < 75:
        n -= 45
        count += 4
        continue
    if n < 45:
        count += (n / 10)
        n = 0

print("%d" % (count))
