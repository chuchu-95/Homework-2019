lst = [1,12, 78, 99, 120, 3, 3, 1, 7,2,11,13]
a = []
d = []
m = []
for i in lst:
    if i == 1:
        continue
    for j in range(2, i):
        if i % j == 0 or i == 1:
            break
    else:
        a.append(i)
for h in a:
    if h not in d:
        d.append(h)
print(d)
shu = 0
chang = len(d)
for y in range(chang):
    for z in range(y+1, chang):
        if d[y]+d[z] in d:
            shu += 1
print(shu)

