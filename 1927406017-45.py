from math import sqrt as q
from math import log as log
def prime(n):
    if 0 not in[n%i for i in range(2, int(q(n)))]:
        return True
    else:
        return False

def meson_prime(n):
    p = log(n+1, 2)
    if prime(n) and p == int(p):
        return int(p)
    else:
        return -1

def print_mesonprime(n):
    p = 2
    a = 2**p - 1
    while a < n:
        if prime(a):
            print("{:>3d},{:>4d}".format(p,a))
            print()
        p += 1
        a = 2**p -1

print(meson_prime(31))
print_mesonprime(1000)


