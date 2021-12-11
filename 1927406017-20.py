lst = [35, 46, 57, 13, 24, 35, 99, 68, 13, 79, 88, 46]
d = []
for i in lst:
    if i not in d:
        d.append(i)
d.sort()
print(d)
