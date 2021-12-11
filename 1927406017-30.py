a, b, c = eval(input("please input 3 int a,b,c: "))
if a <= b:
    if a <= c:
        if b <= c:
            print(a,b,c)
        else:
            print(a,c,b)
    else:
        print(c,a,b)
else:
    if c <= b:
        print(c,b,a)
    else:
        if a <= c:
            print(b,a,c)
        else:
            print(b,c,a)




