from random import randint
def fun1():
    s = {randint(0, 500) for i in range(200)}
    while len(s) <= 200:
        s.add(randint(0, 500))
    return s
def fun2(set):
    count = 0
    for i in set:
        print('{:>5d}'.format(i), end='')
        count += 1
        if count % 10 == 0:
            print()
def func3():
    set1 = fun1()
    set2 = fun1()
    fun2(set1 ^ set2)
    print('\n')
    fun2(set1 & set2)
func3()
