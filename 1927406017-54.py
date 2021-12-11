def remove_num(string, n):
    string_re = list(string)
    string_re.remove(string[n])
    re = ""
    return re.join(string_re)


print(remove_num("python", 3))
