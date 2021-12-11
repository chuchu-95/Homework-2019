def divisor(a):
    lst = []
    for i in range(2, a):
        for j in range(2, a):
            if i * j == a:
                lst.append(i)
    fin = list(set(lst))
    print(sum(fin)+1)


divisor(8)
