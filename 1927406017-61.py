from random import randint
def creat():
    n = randint(0, 9)+1
    return {randint(0,1000) for i in range(n)}
def result(set):
    for i in set:
        print('{:>5d}'.format(i), end='')
    print()
def output(A, B):
    for i in range(3):
        set1 = set(input("A | B:").split())
        set2 = set(input("A & B:").split())
        flag = 0
        if set1 == A | B:
            print("A | B is right")
            flag += 1
        if set2 == A & B:
            print("A & B is right")
            flag += 1
        if flag == 2:
            break
    else:
        print(A | B, A & B, sep='\n')
def main():
    A = creat()
    B = creat()
    result(A)
    result(B)
    output(A, B)
main()
