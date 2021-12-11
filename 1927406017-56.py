def count_appearance(n):
    dic = {}
    li = list(n)
    for i in li:
        dic[i] = dic.get(i, 0) + 1
    b = sorted(dic.items(), key=lambda e: e[1], reverse=True)
    for i in range(len(b)):
        print("\"%s\":%d" %(b[i][0], b[i][1]),end=", ")


count_appearance("google.com")
