lst = []
for i in range(2, 501):
    for j in range(2, i):
        if i % j == 0 and i > 1:
            break
    else:
        lst.append(i)
        print("%3d" %i, end="\t")
        if len(lst) % 5 == 0:
            print("")

