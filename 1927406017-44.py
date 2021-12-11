from math import sqrt as q
def judge_prime(n):
    lst = []
    for i in range(2, int(q(n))):
        if n % i == 0:
            return False
            break
    else:
        return True

def exchange(n):
    n_ex = int(str(n)[::-1])
    return n_ex

def not_palindromic(n):
    if judge_prime(n) != exchange(n):
        return True
    else:
        return False

def inverse_prime(n):
    if judge_prime(n) and judge_prime(exchange(n)) and not_palindromic(n):
        return True
    else:
        return False

def print_prime(n):
    a = 0
    b = 10
    while a <= n:
        if inverse_prime(b):
            print("{:>5d}".format(b), end=" ")
            a += 1
            if a % 8 == 0 and a > 0:
                print()
        b += 1


print(inverse_prime(17))
print_prime(30)








