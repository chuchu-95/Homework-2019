def third_sin(n):
    li = ["o", "ch", "s", "sh", "x", "z"]
    if n[-1] == "y":
        n_re = n[:-1]+"ies"
    elif n[-1] in li:
        n_re = n + "es"
    else:
        n_re = n + "s"
    return n_re

print(third_sin("python"))
