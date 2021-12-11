def two_string(n):
    n_re = ""
    if len(n) < 2:
        return ""
    else:
        l = [n[0],n[1],n[-2::]]
        return n_re.join(l)

print(two_string("python"))
